<script setup>
    import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
    <div>
        <RouterLink to="1">Item1</RouterLink><br>
        <RouterLink to="2">Item2</RouterLink>
        {{ $route.params.id }}
    </div>

</template>