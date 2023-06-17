import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BookList from '../views/BookList.vue'
// ../でも@でもOK
import BookDetail from '@/components/BookDetail.vue'
import NotFound from '@/components/NotFound.vue'
import Item from '../views/Item.vue'
import  User from '@/views/User.vue'
import  UserProfile from '@/components/UserProfile.vue'
import  UserPost from '@/components/UserPost.vue'
import  HomeSub from '@/components/HomeSub.vue'


// const bookinfo = reactive([
//   {id:1, title: 'タイトル1', content:'本の内容1'},
//   {id:2, title: 'タイトル2', content:'本の内容2'},
//   {id:3, title: 'タイトル3', content:'本の内容3'}
// ])


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default:HomeView,
        sub: HomeSub
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/book',
      name: 'bookList',
      component: BookList
    },
    {
      path:'/book/:id',
      name:'Book',
      component:BookDetail,
      // props:true
      props: route => ({ 
        id: Number(route.params.id),
        // title: route.params.title,
        // content: route.params.content
      })
    },
    {
      path:'/item/:id',
      name: 'Item',
      component: Item

    },
    {
      path: '/user',
      component: User,
      children:[
        {
          path:'profile',
          component: UserProfile,
        },
        {
          path:'post',
          component: UserPost,
        }
      ]
    }
    ,
    {
      path: '/:pathMatch(.*)*',
      // redirect: '/'
      name:'Notfound',
      component: NotFound
      
    }
  ]
})

router.beforeEach((to, from, next) => {
  console.log('from', from);
  console.log('to', to);
  next()
})

export default router