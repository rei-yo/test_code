<script setup>

import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

const bookIndex = ref(-1);

const books = reactive([
    {id:1, title: 'タイトル1', content:'本の内容1'},
    {id:2, title: 'タイトル2', content:'本の内容2'},
    {id:3, title: 'タイトル3', content:'本の内容3'}
])

const router = useRouter();

// idしか渡せない。

function showBookDetail(id){
    console.log(id)
    bookIndex.value = id - 1;

    router.push({
        name: 'Book',
        params:{
                id:books[bookIndex.value].id,
                title: books[bookIndex.value].title,
                content: books[bookIndex.value].content
            } 
        }
    )

}

// function bookInfo(){
//     console.log(id)
//     bookIndex.value = id - 1;

//     return{
//         bookdata:{
//                 id:books[bookIndex.value].id,
//                 title: books[bookIndex.value].title,
//                 content: books[bookIndex.value].content
//             } 
//         }
//     }

// export default bookInfo

</script>

<template>
    <div>
        <h1>本の一覧</h1>
        <ul>
            <li @click="showBookDetail(book.id)"
            v-for="book in books" :key="book.id">
                {{ book.title }}
            </li>
        </ul>
    </div>
</template>