<script setup>

const props = defineProps(['agDetail'])

</script>

<template>
    <div class = "AgDetailContents">
        <div class="ag_logo">
            props:{{props.agDetail.agLogo}} <br/>
            props:{{props.agDetail.agSummary}}
    </div>
    </div>
</template>

<style scoped>

.AgDetailContents{
    width: 100vw;
    min-height: 240px;
    border: 1px solid;
}
</style>

