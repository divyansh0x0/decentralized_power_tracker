<script setup lang="ts">
import {onMounted, watch} from 'vue';
import {useThemeManager} from '~/composables/useThemeManager';

const {theme, setTheme} = useThemeManager();

interface PowerData {
    iot_id: string,
    recorded_at: string;
    latitude: number;
    longitude: number;
    pincode: number;
    is_power_available: boolean;
    avg_power_availability: number;
    avg_power_cuts_count: number;
    complaints_count: number;
}

interface TransactionData {
    _id: string;
    power_data: string;
    transaction_id: string;
    verified_on_chain_at: string;
}

async function fetchAllData(): Promise<TransactionData[]> {
    const url = "https://decentralized-power-tracker.onrender.com";
    console.log("Fetching all data");
    const res = await fetch(`${url}/power-data/`);
    const data: any = await res.json();
    console.log("All data:", data);
    return data["data"];
}

onMounted(async () => {
    await import('leaflet/dist/leaflet.css');
    const iot_data = await fetchAllData();
    const L = await import('leaflet');
    const indiaBounds = L.latLngBounds(
        [6.5, 68.0],   // Southwest corner of India
        [37.1, 97.4]   // Northeast corner of India
    );


    const map = L.map('map', {
        center: [21.7679, 78.8718],
        zoom: 5,
        zoomControl: false,
        attributionControl: false,
        maxBounds: indiaBounds,       // restrict panning
        maxBoundsViscosity: 1.0,      // prevent dragging outside
        minZoom: 4.5,                 // prevent zooming out too far
    });

    const lightTiles = L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png',
        {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap & CartoDB',
        }
    );

    const darkTiles = L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
        {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap & CartoDB',
        }
    );

    // Initially add correct theme layer
    let currentLayer = theme.value === 'dark' ? darkTiles : lightTiles;
    currentLayer.addTo(map);

    // Watch for theme changes dynamically
    watch(
        theme,
        (newTheme) => {
            const newLayer = newTheme === 'dark' ? darkTiles : lightTiles;

            if (map.hasLayer(currentLayer)) {
                map.removeLayer(currentLayer);
            }
            newLayer.addTo(map);
            currentLayer = newLayer; // keep track of active layer
        },
        {immediate: false}
    );

    // Load and render GeoJSON
    const response = await fetch('/geo/in.geojson');
    const indiaGeoJson = await response.json();

    const indiaLayer = L.geoJSON(indiaGeoJson, {
        style: {
            color: 'var(--color-accent)',
            weight: 2,
            fillOpacity: 0.1,
        },
    }).addTo(map);

    map.fitBounds(indiaLayer.getBounds());

    function addDataPoint(point: PowerData) {
        console.log(point);
        let point_color = "";
        if (point.avg_power_availability > .85) {
            point_color = "#00ff00";
        } else if (point.avg_power_availability > .50) {
            point_color = "#ffc800";
        } else {
            point_color = "#ff0000";
        }
        const marker = L.circleMarker([point.latitude, point.longitude], {
            radius: 6,
            color: point_color,
            fillColor: point_color,
            fillOpacity: 0.5,
            stroke: false,
        })
            .addTo(map)
            .bindPopup(
                `

        <b>Currently Powered:</b> ${point.is_power_available}<br/>
        <b>Power Availability:</b> ${(point.avg_power_availability * 100).toFixed(2)}%<br/>
        <b>Power Cuts:</b> ${(point.avg_power_cuts_count).toFixed(2)} per week<br/>
        <b>Complaints:</b> ${point.complaints_count}<br/>
        <b>Power availability time:</b> ${(point.avg_power_availability * 24).toFixed(2)} hr/day
`
            );
        marker.on('popupopen', () => {
            marker.setStyle({radius: 10, fillOpacity: 0.8});
        });

        marker.on('popupclose', () => {
            marker.setStyle({radius: 6, fillOpacity: 0.5});
        });
    }

    for (const iot_data_el of iot_data) {
        addDataPoint(JSON.parse(iot_data_el["power_data"]));
    }
});
</script>

<template>
    <div class="map-wrapper">
        <div id="map"></div>
        <h3>Decentralized Power Tracker</h3>
    </div>
</template>

<style scoped>

.map-wrapper {
    position: relative; /* establishes a new stacking context */
    height: 100vh;
    width: 100%;
}

#map {
    height: 100%;
    width: 100%;
}

h3 {
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 1000; /* higher than Leaflet’s tile layers */
    color: white; /* visible on dark map */
    background: rgba(0, 0, 0, 0.4);
    padding: 4px 8px;
    border-radius: 6px;
    font-weight: 500;
}
</style>
