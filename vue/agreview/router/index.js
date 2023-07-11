import { createRouter, createWebHistory } from 'vue-router'
import Route1 from '../components/page/TopPage.vue'
import Route2 from '../components/page/IndeividualAgentReviewPage.vue'
import Route3 from '../components/test/Route3.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'route1',
      component: Route1
    },
    {
      path: '/route2',
      name: 'route2',
      component: Route2
    },
    {
      path: '/route3',
      name: 'route3',
      component: Route3
    },
     
  ]
})


export default router
