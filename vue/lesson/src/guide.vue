<script setup>
    import { reactive, ref } from 'vue'
     
    //テンプレート構文
    const msg = ref("hello world");
    const test_url = ref("https://www.google.co.jp/");
    const test_div = ref('test_div');
    const isButtonDisabled = ref(false);
    const objectOfAttrs = ref({id: 'test_id',class: 'wrapper'});
    const number_temp = ref(1);

    //起動しない関数
    let date_data = new Date();
    let today_data = date_data.setDate(date_data.getDate());
    function time_func(date){
        return date.getDate() + 1;
    } 

    const seen = ref(true);
    function change_text_color_state(){
        this.text_color_state.value = !this.text_color_state.value;
    }

</script>

<style scoped>
    .container{
        display:flex;
        flex-flow: column;
        border: solid 2px black;
        padding: 15px;
        width: 600px;
        border-radius: 10px; 
        justify-content: center;
        }
    
    #red-text  {
        color:red;
    }

    
</style>

<template>
    <div class="container">
        <h3>テンプレート構文</h3><br>
        <ul>
            <li>Message: {{ msg }}</li>
            <li>text interpolation:{{ test_url }} </li>
            <li>リンクを作るとき（v-html) <a :href = "test_url" v-html=test_url></a></li>
            <li :id="red-text">v-bind test</li>
            <button :disabled="isButtonDisabled">Button</button>
            <li v-bind="objectOfAttrs">複数の属性を動的にバインドさせる</li>
            <li>マスタッシュ構文内でjavascriptの式も使用可能 例：{{ number_temp + 1}}</li>
            <li><p v-if="seen">seenがtrueの場合に表示</p></li>
            <li>v-on演習：<button :id ="{red_text: text_color_state}" @click="change_text_color_state"> クリックすると赤字になる </button></li>
        </ul>
    </div>
</template>
