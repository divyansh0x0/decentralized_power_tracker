// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  ssr: true,
  content: {
    experimental: { nativeSqlite: true },
  },
  devtools: { enabled: false },
  nitro: {
    preset: 'vercel'
  },
  compatibilityDate: '2025-07-15',
  css:[
    'leaflet/dist/leaflet.css',

    "~/assets/scss/main.scss",
    "~/assets/styles/default.css",
    "~/assets/styles/main.css",
    "~/assets/styles/theme.css",

  ],
  modules: [
    '@nuxt/content',
    '@nuxt/eslint',
    '@nuxt/image',
    '@nuxt/scripts',
  ],
})