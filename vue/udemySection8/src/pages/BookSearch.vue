<script setup>
import { ref } from 'vue'

const keyword = ref('')
const searchResults = ref([])

const emit = defineEmits(['add-book-list'])

function addBookList(index){
    emit('add-book-list', searchResults.value[index])
}


async function search(keyword){
    console.log("search function called")
    searchResults.value.splice(0, searchResults.value.length);

    const baseUrl = 'https://www.googleapis.com/books/v1/volumes?'
    const params = {
        q:`intitle:${keyword}`,
        maxResults:40
    }
    const queryParams = new URLSearchParams(params)
    console.log(baseUrl+queryParams)

    const response = await fetch(baseUrl + queryParams)
    .then( response => response.json())

    console.log(response.items)

    if (response.items){
        for(let book of response.items){
            let title = book.volumeInfo.title
            let img = book.volumeInfo.imageLinks
            let description = book.volumeInfo.description
            searchResults.value.push({
                title: title? title:'',
                image: img ? img.thumbnail:'',
                description: description ? description.slice(0, 40): ''
            })
        }
    }
}

</script>

<template>
    <v-row>
        <V-col cols="6">
            <v-text-field label="本のタイトルを検索" v-model="keyword"></v-text-field>
        </V-col>
    </v-row>
    <v-row>
        <V-col cols="3">
            <v-btn class = "ml-3" color="primary" @click="search(keyword)">検索する</v-btn>
        </V-col>
        <v-col cols="3">
            <v-btn color="secondary" to="/">一覧に戻る</v-btn>
        </v-col>
    </v-row>
        
    <v-row>
        <v-col cols="12" md="6" 
        v-for="(book,index) in searchResults" :key="book.index">
            <v-card class = "mx-auto">
                <v-row>
                    <v-col cols="4">
                        <v-img :src="book.image"></v-img>
                    </v-col>
                    <v-col cols="8">
                        <v-card-title>{{ book.title }}</v-card-title>
                        {{ book.description }}
                        <v-spacer></v-spacer>
                        <v-col cols="auto">
                            <v-btn 
                            icon="mdi:mdi-plus" color="indigo" size="small"
                            @click="addBookList(index)">
                            </v-btn>
                        </v-col>
                    </v-col>
                </v-row>
            </v-card>
        </v-col>
    </v-row>










</template>