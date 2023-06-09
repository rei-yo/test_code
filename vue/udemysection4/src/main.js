import './assets/main.css'

import { createApp } from 'vue'
import Section4GlobalCompo from './Section4_51_global.vue'
import App from './Section4_Root.vue'


const app = createApp(App)


app.component('GlobalComponent', Section4GlobalCompo).mount('#app')