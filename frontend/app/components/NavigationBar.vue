<script setup lang="ts">
import { Icon } from "@iconify/vue";

interface NavLink {
    name: string,
    url: string,
    icon: string
}

const links: NavLink[] = [
    {
        name: "Map",
        url : "/",
        icon: "mdi:map"
    },
    {
        name: "Complaints",
        url : "/complaint",
        icon: "streamline-freehand:customer-action-complaint"
    }
];
import { useRoute } from 'vue-router';
const route = useRoute();

</script>

<template>
    <div class="nav-bg-overlay"></div>
    <nav class="navbar">
        <!--        <div>-->
        <ul class="nav-links">
            <li v-for="link in links" :key="link.name">
                <a :href="link.url" class="nav-link" :class="{ active: route.path === link.url }">
                    <Icon class="nav-link-icon" :icon="link.icon"/>
                    <span class="nav-link-name">{{ link.name }}</span>
                </a>
            </li>
        </ul>

    </nav>
</template>

<style scoped lang="scss">
.nav-bg-overlay {
    z-index: 999998;
    position: fixed;
    height: 100vh;
    width: 100vw;
    background-color: rgba(0, 0, 0, 0.45);
    display: none;
}

.navbar {
  backdrop-filter: blur(10px) brightness(150%);
  border-radius: var(--border-radius-sm);
    user-select: none;
    background: none;
    z-index: 999999;
    bottom: 10px;
    left: 50%;
  transform: translateX(-50%);
    position: fixed;
    display: flex;
    justify-content: space-between;
    height: fit-content;
    width: fit-content;
    padding: 0;

}


.nav-links {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;

    li {
        list-style: none;
    }
}

.nav-link {
    text-align: center;
    display: block;
    width: 100%;
    height: 100%;
    color: var(--color-on-surface);
  padding: 1em;
    &.active{
        color: var(--color-accent);
    }
}

.nav-link-name {
    display: none;
}

.nav-link-icon {
    display: block;
    font-size: 2em;
    //width: 100%;
}

</style>