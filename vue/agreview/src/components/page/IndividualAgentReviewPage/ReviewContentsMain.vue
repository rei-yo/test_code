<script setup>
    import ReviewContentsMenuTab from './ReviewContentsMenuTab.vue'
    import ReviewContentsLeft from './ReviewContentsLeft.vue'
    import ReviewContentsRight from './ReviewContentsRight.vue'

    const props = defineProps(["AgEvaluation"])

</script>

<template>
    <div class = ReviewContentsMain>
        <ReviewContentsMenuTab/>
        <div class = "AgDetailContents">
            <div class="detail">
                <ReviewContentsLeft :AgEvaluation="props.AgEvaluation"/>
                <ReviewContentsRight />   
            </div>
        </div>
    </div>
</template>

<style scoped>

.ReviewContentsMain {
    height: 100vh;
    border: 1px solid;
}

.AgDetailContents{
    display:flex;
}

</style>
