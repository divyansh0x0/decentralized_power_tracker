<script setup lang="ts">


import PowerMap from "~/components/PowerMap.vue";

async function addPowerData() {
  const res = await fetch("http://127.0.0.1:8000/power-data/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      iot_id: "IOT-123",
      recorded_at: new Date().toISOString(),
      latitude: 22.9734,
      longitude: 78.6569,
      pincode: 482001,
      power_availability: 1,
      number_power_cuts: 2,
      number_complaints: 0,
    }),
  });

  const data = await res.json();
  console.log("Response:", data);
}
async function fetchAllData() {
  const res = await fetch("http://127.0.0.1:8000/power-data/");
  const data = await res.json();
  console.log("All data:", data);
}
fetchAllData();

</script>
<template>
    <main>
      <PowerMap class="odd-section" />
    </main>
</template>
<style scoped>
.odd-section{
    background-color: var(--color-surface-container-lowest);
}
.even-section{
    background-color: var(--color-surface-container-low)
}
</style>
