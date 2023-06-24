<script setup>
import HeaderVue from '@/components/globals/Header.vue'
import ReviewContentsMain from './IndividualAgentReviewPage/ReviewContentsMain.vue'
import AgDetailContents from './IndividualAgentReviewPage/AgDetailContents.vue'


const agSummary = "agent summary"
const agLogo = "agent logo"
const agDetail = {"agSummary":agSummary, "agLogo": agLogo}

const graphData = "graph data"
const AgEvaluationTable = "agent evaluation table"
const AgEvaluation = {"graphData": graphData,
                      "AgEvaluationTable": AgEvaluationTable}




</script>

<template>
    <header>
        <HeaderVue/>
    </header>
    <div class="contents">
        <div class = "AgDetailContents">
            <AgDetailContents :agDetail="agDetail"/>
        </div>
        <div class = "ReviewContentsMain">
            <ReviewContentsMain :AgEvaluation="AgEvaluation"/>
        </div>
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