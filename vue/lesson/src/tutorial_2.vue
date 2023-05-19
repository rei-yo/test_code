<script>

//componentのimport
import ChildComp from "./components/CompTest.vue"


// id用の変数
let id = 0

export default {
    data() {
        return {
            newTodo: '',
            hideCompleted: false,
            todos: [
                { id: id++, text: 'Learn HTML' },
                { id: id++, text: 'Learn JavaScript' },
                { id: id++, text: 'Learn Vue' }
            ],

            watch_data:{
                todoId:1,
                todoData:null
            },

            greeting: 'Hello from parent',
            childMsg: 'No child msg yet',
            parent_msg:'from parent data'
        }
    },

    methods: {
        addTodo() {
            this.todos.push({ id: id++, text: this.newTodo })
            this.newTodo = ''
        },

    
        removeTodo(todo) {
            this.todos = this.todos.filter((t) => t !== todo)
        },

        completed:{
            filterdTodos(){
                return this.hideCompleted ? this.todos.filter((t) => !t.done):this.todos 
            }
        },

        async fetchData(){
            this.todoData = null;
            const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${this.watch_data.todoId}`);
            this.todoData = await res.json();
            }
    },

    mounted() {
        //マウントされた後にアクセス
        this.$refs.p.textContent = 'mounted!';
        this.fetchData();
    },

    components: {
    ChildComp
    }

}
</script>

<template>
    <!-- @submitで指定したmethodに送信。.preventでformに設定されている処理を実施しない-->
    <form @submit.prevent="addTodo">
        <input v-model="newTodo">
        <button>Add Todo</button>    
    </form>

    <ul>
    <!-- -->
        <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" v-model="todo.done">
            <span :class="{ done: todo.done }" > {{ todo.text }} </span>
            <button @click="removeTodo(todo)">X</button>
        </li>
    </ul>
    <button @click="hideCompleted = !hideCompleted">
        {{ hideCompleted ? 'Show all' : 'Hide completed' }}
    </button>

    <p>Todo id: {{ watch_data.todoId }}</p>
    <button @click = "watch_data.todoId ++ "> fech next todo </button>
    <p v-if = "!watch_data.todoData"> Loading...</p>
    <pre v-else> {{ watch_data.todoData }} </pre>

    <p ref="p"> hello </p>

    <!--v-on:<イベント名>または@<イベント名>でイベント監視 -->
    <ChildComp :msg="greeting" @response="(parent_msg) => childMsg = parent_msg">
        from parent: {{ parent_msg }}
    </ChildComp>
    <p>{{ childMsg }}</p>
</template>

<style>
    .done{
        text-decoration: line-through;
    }
</style>