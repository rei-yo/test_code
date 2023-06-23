<script setup>
import HeaderVue from '@/components/globals/Header.vue'
import ReviewContentsMain from './IndividualAgentReviewPage/ReviewContentsMain.vue'
import AgDetailContents from './IndividualAgentReviewPage/AgDetailContents.vue'

</script>

<template>
    <header>
        <HeaderVue/>
    </header>
    <div class = "AgDetailContents">
        <AgDetailContents/>
    </div>
    <div class = "ReviewContentsMain">
        <ReviewContentsMain/>
    </div>
</template>

<style scoped>

header {
      margin: auto;
      width: 100vw;
      max-height: 200 px;
      text-align: center;
    }

.AgDetailContents{
    margin: auto;
    width: 80vw;
    text-align: center;
}
.ReviewContentsMain{
    margin:auto;
    width: 80vw;
    text-align: center;
}



</style>