<script setup>


import { ref, reactive, computed, onMounted, watch } from 'vue'
import { useStore, mapState, mapActions } from 'vuex'
import { useRouter } from 'vue-router'


const store = useStore()
const router = useRouter()
const loginUser = reactive({
  id: -1,
  name: '',
  isVisible: false,
});
const loginAction = (user) => store.dispatch('auth/loginAction', user)
function login() {
  const userId = 1
  loginUser.value = store.getters.getUserById(userId)
  loginAction(loginUser.value)
  router.push('/setting')
}

function doLogin(user) {
}

</script>

<template>
  <div class="login">

    <div class="contents">
      <h2><span style="text-decoration: overline;">Login</span></h2>
      <div style="display:flex; justify-content: center;">
        <div style="display:flex;padding-top:0.5rem;">
          <div style="min-width: 24px;margin:0 1rem">ユーザー名:</div>
          <div><input readonly value="大谷" 
            style="background-color: lightgray;border-radius: 4px; border-style:none;"/></div>
        </div>
      </div>
      <div style="display:flex; justify-content: center;">
        <div style="display:flex;padding-top:0.5rem;">
          <div style="min-width: 24px;margin:0 1rem">パスワード:</div>
          <div><input value="test"
            style="background-color: lightgray;border-radius: 4px; border-style:none; ;"/></div>
        </div>
      </div>
      <div style="margin-top: 1.25rem; display:flex; justify-content: center;">
        <button @click="login" style="border-radius: 4px; border: 1px solid gainsboro;padding:0.25rem 0.75rem; cursor: pointer;">ログイン</button>
      </div>

    </div>

  </div>
</template>