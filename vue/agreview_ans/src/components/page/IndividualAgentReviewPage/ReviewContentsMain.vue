<script setup>
    import ReviewContentsMenuTab from './ReviewContentsMenuTab.vue'
    import ReviewContentsLeft from './ReviewContentsLeft.vue'
    import ReviewContentsRight from './ReviewContentsRight.vue'
    import { useRouter } from 'vue-router'

    const props = defineProps(["AgEvaluation"])


    const router = useRouter()
    function selectTabMenu(e) {
        console.log('Review',e)
        switch (e){
            case 1:
                router.push('/')
                break
            case 2:
                router.push('/route2')
                break
            case 3:
                router.push('/route3')
                break
            defalut:
                router.push('/')
        }
    }

</script>

<template>

    <RouterView />
    
    <div class = ReviewContentsMain>
        <ReviewContentsMenuTab @select-tab="selectTabMenu"/>
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
