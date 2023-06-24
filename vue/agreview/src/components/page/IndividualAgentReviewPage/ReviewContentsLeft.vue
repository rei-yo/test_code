<script setup>
import { ref } from 'vue'

const props = defineProps(['AgEvaluation'])

const categories = ref([
    {id: 1, category:'サービスの特徴'},
    {id: 2, category:'お勧めする人'},
    {id: 3, category:'良い点'},
    {id: 4, category:'悪い点'}
])

</script>


<template>
    <div class="review_content_left">
        <div class="chart_contents">
            graph area <br/>
            props:{{ props.AgEvaluation.graphData }}
            
        </div>
        <div class="evaluation_contents">
            evaluation area<br/>
            props:{{ props.AgEvaluation.AgEvaluationTable }}
            
        </div>
        <div>
            <div v-for="category in categories" :key="category.id" class = "category">
                <a href="#">{{ category.category }}</a>
            </div>
        </div>
        <div class = "review">
            口コミ内容
        </div>
    </div>
</template>

<style scoped>
.review_content_left{
    margin:10px;
}

.chart_contents {
  display : inline-block;
  width: 240px;
  min-height: 240px;;
  background-color: #FFFFFF; 
  border: solid;
  margin: 4px;
}
.evaluation_contents{
    display: inline-block;
    width: 400px;
    min-height: 240px;
    border:solid;
}

.category{
    margin: 4px;
    min-height :40px;
    display: inline-block;
    border: 1px solid;
    width:320px;
}

.review{
    width:650px;
    height: 450px;
    margin:4px;
    border: 1px solid;
    display:inline-block
}

</style>
  