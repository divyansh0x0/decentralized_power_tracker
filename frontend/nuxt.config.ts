// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  ssr: true,
  content: {
    experimental: { nativeSqlite: true },
  },
  nitro: {
    preset: 'vercel'
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
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