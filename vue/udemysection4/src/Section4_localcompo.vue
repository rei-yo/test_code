<script setup>
    import Section4_51_props from './components/Section4_51.vue'
    import ArrayTest from './components/Section4_array.vue'
    import EmitTest from './components/emit_test.vue'
    import CustomInput_58 from './components/Section4_58_Form.vue'

    const parentTitle = '親側のタイトル'

    const members = [
        {name: '久保'},
        {name: '南野'},
        {name: '堂安'},
    ]

    
    function parentMethod(e, e2) {
        console.log([e, e2])
    }

    let countNum = 1;
    function parentMethod2(e) {
        countNum = countNum + e;
    }

    const parentValue = ref('');

</script>

<template>
    <div>local component</div>

    <div class="lesson">
        <div>●親側で属性値にtitleを定義し、データを子へ</div>
        <Section4_51_props title="親→子へのデータ"/>
        <Section4_51_props disabled='true' />
    </div>

    <div class="lesson">
        <div>●親側で変数を定義し、v-bindで変数を子へ</div>
        <Section4_51_props :title="parentTitle"/>
    </div>

    <div class="lesson">
        <div>●propsで配列を渡す</div>
        <ArrayTest class = 'child'
        v-for = "member in members"
        :key="member.name"
        :item="member"
        />
    </div>

    <!-- defineEmitsで2つ以上のmethodを定義したり、複数のcustomEventを登録することは可能なのか？-->
    <div class="lesson">
        <div>●emitで子から親にデータを渡す</div>
        <EmitTest @customEvent = "parentMethod" @customEvent2 = "parentMethod2"/>
        <div>  {{ countNum }}  </div>
    </div>


</template>

<style scoped>

    .lesson {
        width: 100%;
        border: solid 3px;
        border-radius: 10px ;
        padding: 20px;
        margin: 10px;
    }

</style>