<script setup>
import { storeKey } from 'vuex';
import { useStore, mapActions } from 'vuex'
const store = useStore()

defineProps({
  msg: {
    type: String,
    required: true
  }
})

// function addCount(){
//   store.commit('addCount', {
//     value:10
//   })
// }

function addCount(){
  store.dispatch('addCountAction',{
    value:10
  })
}



</script>

<template>
  <div>
    <button @click="addCount">+10</button>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
