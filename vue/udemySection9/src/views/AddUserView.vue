<script setup>
//import TheWelcome from '../components/TheWelcome.vue'
import { ref, reactive, computed, onMounted, watch } from 'vue'
import { useStore, mapState, mapActions } from 'vuex'
const store = useStore()
const count = computed(() => {
  return store.state.count
})
const allUsers = computed(() => store.getters.allUsers )
const maxUserId = computed(() => store.getters.getMaxUserId )
const newUser = reactive({
  id: -1,
  name: '',
  isVisible: true,
});
function addUser() {
  newUser.id = maxUserId.value + 1
  const user = new Object()
  user.id = newUser.id
  user.name = newUser.name
  user.isVisible = newUser.isVisible
  store.dispatch('addUserAction', user)
  newUser.name = ''
}
</script>

<template>
  <main>
    <!-- <TheWelcome /> -->
    <h2><span style="text-decoration: overline;">Add user </span></h2>
    <div style="margin-top:1rem;">
      ユーザーを追加します
    </div>

    <div style="background-color: honeydew;font-weight: bold;margin-top:1rem; padding:0.5rem;">ユーザー一覧</div>
    <div>
      <ul>
        <li v-for="user in allUsers" :key="user.id">
          {{ user.id }} : {{ user.name }} : {{ user.isVisible }} 
        </li>
      </ul>
    </div>

    <div style="background-color: honeydew;font-weight: bold; margin: 0.7rem 0; padding:0.5rem;">追加ユーザー
      <div style="display:flex;padding-top:0.5rem;">
        <div style="min-width: 64px;margin:0 1rem">id:</div>
        <div>{{ maxUserId + 1 }}</div>
      </div>
      <div style="display:flex;padding-top:0.5rem;">
        <div style="min-width: 64px;margin:0 1rem">名前:</div>
        <div><input v-model="newUser.name"/></div>
      </div>
      <div style="display:flex;padding-top:0.5rem;">
        <div style="min-width: 56px; margin:0 1rem">表示可否:</div>
        <div><input type="checkbox" v-model="newUser.isVisible">表示</div>
      </div>
      <div style="display:flex;padding:0.75rem;">
        <button @click="addUser()" >追加</button>
      </div>
    </div>



  </main>
</template>