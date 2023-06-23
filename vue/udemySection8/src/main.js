import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, fa } from 'vuetify/iconsets/fa'
import { mdi } from 'vuetify/iconsets/mdi'


const vuetify = createVuetify({
    components,
    directives,
    icons: {
      defaultSet: 'fa',
      aliases,
      sets: {
        fa,
        mdi,
      },
    },
  })

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.mount('#app')
