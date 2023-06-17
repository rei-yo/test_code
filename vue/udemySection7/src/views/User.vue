<script setup>

</script>

<template>
    <div>
        ユーザー情報<br>
        <router-link to="profile">プロフィール</router-link> | 
        <router-link to="post">記事</router-link> | 
        <div class="green-b">
            <router-view></router-view>
        </div>
    </div>
</template>

<style scoped>
    .green-b{
        border:1px solid green;
    }
</style>