<script setup>
import { useRoute, useRouter } from 'vue-router'
import { onBeforeRouteLeave } from 'vue-router'


onBeforeRouteLeave((to, from, next) =>{
  const checkLeave = window.confirm('このページを離れますか？')
  if(checkLeave){
    next();
  } else {
    next(false)
  }
})

const route = useRoute()
const router = useRouter()


function checkRouteInfo() {
  console.log(route)
  console.log(router)
} 

function goToHome() {
  router.push('/')
}

</script>


<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="checkRouteInfo">ルート情報</button>
    <button @click="goToHome">Homeに戻る</button> 
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
