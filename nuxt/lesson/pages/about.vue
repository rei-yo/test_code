<script setup>

import { ref, computed, onMounted, watch } from 'vue'
const subtitle = ref("test doc from about.vue")

</script>

<template>
    <div>
        <h1>about page</h1>
        <h2>{{ subtitle }}</h2>
    </div>
</template>