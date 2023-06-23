<script setup>

import { ref } from 'vue'

const props = defineProps({
  'books': {
    type: Array,
    default: ()=>{[]}
  }
})

defineEmits(['add-book-list', 'update-book-info'])

const books = ref(props.books)

</script>

<template>
<div>
    <v-row>
        <v-col cols="6">
            <v-btn color="primary" to="/search">検索する</v-btn>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="12" sm="6" v-for="book in books" :key="book.id">
            <v-card>
                <v-row>
                    <v-col cols="4">
                        <v-img :src="book.image"></v-img>
                    </v-col>
                    <v-col cols="8">
                        <v-card-title>{{ book.title }}</v-card-title>
                        読んだ日：{{ book.readDate }}
                        感想：{{ book.memo }}
                        <v-spacer></v-spacer>
                        <v-btn :to="{ name:'BookEdit', params:{id: book.id} }"
                        color = "indigo" fab small dark>
                        <b-icon>mdi-pencil</b-icon>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card>
        </v-col>
    </v-row>


</div>
</template>