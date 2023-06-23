import { createRouter, createWebHistory } from 'vue-router'
import BookSearch from '@/pages/BookSearch.vue'
import BookIndex from '@/pages/BookIndex.vue'
import BookEdit from '@/pages/BookEdit.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'bookindex',
      component: BookIndex
    },
    {
      path: '/search',
      name: 'booksearch',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: BookSearch
    },
    {
      path: '/edit/:id',
      name: 'bookedit',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: BookEdit
    },
    {
      path:'/:pathMatch(.*)*',
      redirect: '/'
    }
  ]
})

export default router
