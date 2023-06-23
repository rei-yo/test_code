<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import '@vuepic/vue-datepicker/dist/main.css'
import VueDatePicker from '@vuepic/vue-datepicker';
import { ja } from 'date-fns/locale';
const route = useRoute()

const props = defineProps({
    'books':{
        type: Array,
        default:() =>{[]}
    }
})

const date = ref(props.books[route.params.id].readDate)
const book = ref(props.books[route.params.id])
const emit = defineEmits(['update-book-info'])

function updateBookInfo(){

    let readDate = ''
    if (date.value) {
    readDate = new Date(date.value).toLocaleDateString()
    }

    console.log("readdate", readDate)

    emit('update-book-info',{
        id: route.params.id,
        readDate: readDate,
        memo: book.value.memo
    })
}

console.log("bookedit", props.books[route.params.id])

</script>

<template>
    <div>
        <v-row>
            <v-col cols="12">
                <v-card class="mx-auto">
                    <v-row>
                        <v-col cols="4">
                            <v-img :src="book.image"></v-img>
                        </v-col>
                        <v-col cols="8">
                            <v-card-title>
                                タイトル：{{ book.title }}
                            </v-card-title>
                            <v-card-text>
                                読んだ日：
                                <VueDatePicker
                                v-model="date" 
                                :enable-time-picker="false"
                                :auto-position="false"
                                :format-locale="ja" 
                                format="yyyy/MM/dd" 
                                style="width:240px; margin:1rem;"></VueDatePicker>

                                感想：<v-textarea bg-color="" color="" active-color="red"
                                class="mx-2" v-model="book.memo">
                                {{book.memo }}
                                </v-textarea>
                            </v-card-text>

                            <v-card-actions>
                            <v-btn color="secondary" to="/">一覧に戻る</v-btn>
                            <v-btn color="info" 
                            @click="updateBookInfo">保存する</v-btn>
                            </v-card-actions> 

                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </div>
    <div>edit</div>
    <div>{{ books }}</div>
</template>