<script setup lang="ts">


import PowerMap from "~/components/PowerMap.vue";
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
