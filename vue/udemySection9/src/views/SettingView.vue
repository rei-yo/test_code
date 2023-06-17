<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const count = computed(() => {
  return store.state.count
})
const visibleUsers = computed(() => store.getters.visibleUsers )
const unVisibleUsers = computed(() => store.getters.unVisibleUsers )
const editUserId = ref(-1)
function addCount() {
  console.log('increment from HomeView.vue')
  store.commit('addCount', 10)
}
const storeDebug = ref(false)
const editUser = reactive({
  id: -1,
  name: '',
  isVisible: false,
});
function selectUser(id) {
  editUserId.value = id
  console.log(store.getters.getUserById(id))
  editUser.value = store.getters.getUserById(id)
}
</script>

<template>
  <main>
    <!-- <TheWelcome /> -->
    <h2><span style="text-decoration: overline;">Setting</span></h2>
    <div style="margin-top:1rem;">↓ ここを押すと
      <span 
        style="color:indianred; font-size: large; font-weight: bold; margin:0 0.25rem;">
        10
      </span>
      増えます
    </div>
    <div style="display:flex;">
      
      <div @click="addCount" style="margin:0.5rem 1rem;cursor: pointer;">
        <img class="logo" src="@/assets/press.png" width="48" height="48" />
      </div>

      <div style="margin:1rem;">
        count: {{ count }}
      </div>

    </div>
    <div style="background-color: honeydew;font-weight: bold; padding:0.5rem;">ユーザー</div>
    <div>
      <ul>
        <li v-for="user in visibleUsers" :key="user.id">
          {{ user.id }} : {{ user.name }} : {{ user.isVisible }} 
          <span style="margin:1rem">
            <button v-if="user.id != editUserId" @click="selectUser(user.id)" >編集</button>
            <span v-if="user.id == editUserId" style="font-weight: bold;color: darkcyan">編集中</span>
          </span>
        </li>
      </ul>
    </div>
    <div style="background-color: gainsboro; margin:1rem 0;">
      <ul>
        <li v-for="user in unVisibleUsers" :key="user.id">
          <span style="text-decoration: line-through;">{{ user.id }} : {{ user.name }} : {{ user.isVisible }}</span>
          <span style="margin:1rem">
            <button v-if="user.id != editUserId" @click="selectUser(user.id)" >編集</button>
            <span v-if="user.id == editUserId" style="font-weight: bold;color: darkcyan">編集中</span>
          </span>
        </li>
      </ul>
    </div>
    <div v-if="editUser.value" style="background-color: honeydew;font-weight: bold; margin: 0.7rem 0; padding:0.5rem;">編集中
      <div style="display:flex;padding-top:0.5rem;">
        <div style="min-width: 64px;margin:0 1rem">名前:</div>
        <div><input v-model="editUser.value.name"/></div>
      </div>
      <div style="display:flex;padding-top:0.5rem;">
        <div style="min-width: 56px; margin:0 1rem">表示可否:</div>
        <div><input type="checkbox" v-model="editUser.value.isVisible">表示</div>
      </div>  
    </div>
    
    <div style="background-color: floralwhite;font-weight: bold; margin: 0.7rem 0; padding:0.5rem;">Storeデバッグ
      <button v-if="storeDebug" @click="storeDebug = !storeDebug" >非表示</button>
      <button v-if="!storeDebug" @click="storeDebug = !storeDebug">表示</button>
      <div v-if="storeDebug">
        {{ store }}
      </div>
    </div>


  </main>
</template>