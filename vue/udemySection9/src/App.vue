<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { useStore } from 'vuex'
import { ref, computed, onMounted, watch } from 'vue'


const store = useStore()

// function increment() {
//   console.log('increment from App.vue')
//   store.commit('increment')
// }

function increment(){
  console.log('incrementAction from App.vue')
  store.dispatch('incrementAction')
}


const visibleUsers = computed(() => {
  return store.getters.visibleUsers
})

const getUserById = computed(() => {
  return store.getters.getUserById(2)
})

const name = {loginUserName: 'testname'}

const loginAction = ()=>store.dispatch('auth/loginUser', name)



</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
      <div>
        <HelloWorld msg="You did it!" />
        <button @click="increment">+</button>
        {{ store.state.count }}<br>  
        <button @click ="loginAction">ログイン名表示</button>
      </div>
      
      <div>
        <ul>
          <li v-for="user in visibleUsers" key="user.id">
            {{ user.id }} : {{ user.name }}
          </li>
        </ul>
      </div>
      <br>
        
      <div>{{ getUserById }}</div>
    </div>

  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
