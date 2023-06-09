<script setup>

    const props = defineProps({
        'item':{},
    })

</script>

<template>

    <div>
        <p> {{ item.name }}</p>
    </div>

</template>