import { createStore } from 'vuex'
import auth from "./auth"

const store = createStore({
    state(){
        return {
            count: 0,
            users:[
                {id:1, name :"大谷",isVisible:true},
                {id:2, name :"錦織",isVisible:true},
                {id:3, name :"ダルビッシュ",isVisible:false}
            ]
        }
    },

    mutations:{
        increment(state) {
            state.count++
        },

        addCount(state, payload){
            // payloadはオブジェクト
            state.count += payload.value
        },
    },

    actions: {
        incrementAction ({commit}) {
          commit('increment')
        },

        addCountAction({commit}, payload){
            commit('addCount', payload)
        }
    },

    getters: {
        visibleUsers: state => state.users.filter( user => user.isVisible),
    
        getUserById: state => id => {
            return state.users.find( user => user.id === id )
          },
    },

    modules: {
        auth,
    }
})


export default store