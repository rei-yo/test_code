<script setup>

    import LocalComponent from './Section4_localcompo.vue'

</script>

<template>
    <div class = "global_compo">
        <GlobalComponent/>
    </div><br>
    <div  class = "child_compo">
        <LocalComponent/>
    </div>
</template>

<style scoped>

    .global_compo {
        width: 80%;
    }

    .child_compo {
        width: 500px;
    }

</style>