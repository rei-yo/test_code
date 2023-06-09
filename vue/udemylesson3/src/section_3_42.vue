<script setup>

    import { ref, reactive, computed } from 'vue'

    const  newItem = ref("")
    const  query = ref("")
    const todos = reactive([])

    function addItem(){
        if(!newItem.value) return
            const todo = {
                item:newItem.value,
                isDone: false,
            }
        
        todos.push(todo)
        newItem.value = ""
    }

    function deleteItem(index){
        todos.splice(index, 1)
    }

    const filteredList = computed(() => {
        return todos.filter( todo => { return todo.item.indexOf(query.value) !== -1 } )
    })


</script>

<template>

    <input type="text" v-model="newItem">
    <button @click.prevent="addItem">追加</button>
    <input v-model="query">検索


    <ul v-cloak>
        <li v-for="(todo, index) in filteredList">
            <input type="checkbox" v-model="todo.isDone">
            <span :class="{done: todo.isDone}">{{ todo.item }}</span>
            <button @click="deleteItem(index)"> 削除</button>
        </li>
    </ul>

</template>

<style scoped>

    [v-cloak]{
        display:none
    }


    ul{
        list-style: none;
    }

    .done{
        text-decoration: line-through;
    }

</style>