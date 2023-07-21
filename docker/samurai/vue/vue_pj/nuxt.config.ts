// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['/assets/css/style.css'],
  app: {
    // pageTransition:{name :'page', mode: 'out-in'},
    head:{
      title: 'Nuxt 3 basic',
      meta: [{name: 'description', content:'Nuxt 3 for beginner'}],
      link:[{rel:'icon', href:'/icon.png'}],
    }
  }
})
