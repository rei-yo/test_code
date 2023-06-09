<script setup>
    import {ref, reactive, computed, watch} from 'vue';
    import { debounce } from 'lodash';

    const url = "https://dog.ceo/api/breeds/image/random"
    const options = {
        method : 'get'
    }

    async function getDogImage(){
        const response = await fetch(url, options)
        .then( response => response.json() )
        dogImage.value = response.message
    }

    const dogImage = ref('')
    const watchTest = ref('')

    let watchDogImage = debounce(getDogImage, 1000)


    watch(watchTest, async () => {
        watchDogImage()
    })

</script>

<template>
    <button @click="getDogImage">画像取得</button>
    <img :src="dogImage">
    <input type="text" v-model="watchTest">
</template>