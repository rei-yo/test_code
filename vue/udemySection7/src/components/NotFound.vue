<script setup>
    import { useRouter } from 'vue-router'

    const router = useRouter()

    function goToHome() {
        router.push('/')
    }
    

</script>

<template>
    <div>
        ページが存在しません。
    </div>
    <button @click="goToHome">Home</button>
</template>