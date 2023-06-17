import { createStore } from 'vuex'

const state ={
    loginUserName: ""
}

const mutations ={
    loginUser(state, payload){
        state.loginUserName = payload
    },
    logoutUser(state, payload){
        state.loginUserName = null
    }
}

const actions = {
    loginAction({commit}, payload){
        console.log('auth loginAction called')
        commit('loginUser',payload)
    },
    logoutAction({commit}){
        console.log('auth loggoutAction called')
        commit('logoutUser')
    }
}

const getters = {
    getLoginUser (state){
        console.log('auth getLoginUser called')
        return state.loginUser
    },
    isLogin(state){
        console.log('auth isLogin called')
        return (state.loginUser !== null) ? true:false
    }
}

export default {
    namespaced:true,
    state,
    mutations,
    actions,
    getters
}