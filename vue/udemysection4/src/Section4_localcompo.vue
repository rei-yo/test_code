<script setup>
    import { ref } from "vue"
    import Section4_51_props from './components/Section4_51.vue'
    import ArrayTest from './components/Section4_array.vue'
    import EmitTest from './components/emit_test.vue'
    import CustomInput_58 from './components/Section4_58_Form.vue'
    import CustomInput_59 from './components/Section4_59_Form.vue'
    import SlotCompo_62 from './components/Section4_62_slot.vue'
    import SlotCompo_63 from './components/Section4_63_namedslot.vue'
    import SlotCompo_64 from './components/Section4_64_scopedslot.vue'

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
    const parentValue1 = ref('');
    const parentValue2 = ref('');

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

    <div class="lesson">
        <div>●コンポーネント間のフォーム $eventで子からのデータを受け取れる。</div>
        <CustomInput_58 :value="parentValue" @input="parentValue = $event.target.value"/>
        {{ parentValue }}
        <div>●親がv-modelを使用</div>
        <CustomInput_58 class="child" v-model:value="parentValue1"/> 
        {{ parentValue1 }}
    </div>

    <div class="lesson">
        <div>●コンポーネント間のフォーム_子がv-modelを使用</div>
        <CustomInput_59 :value="parentValue2" @input="parentValue2 = $event.target.value"/>
        {{ parentValue2 }} 
    </div>

    <div class="lesson">
        <div>●slot 親から子へデータの差し込み</div>
        <SlotCompo_62>parent</SlotCompo_62>
    </div>

    <div class="lesson">
        <div>●slot 名前付き</div>
        <SlotCompo_63>
            <template v-slot:header>親ヘッダー</template>
            <template #footer>親フッター</template>
        </SlotCompo_63>
    </div>

    <div class="lesson">
        <div>●slot scoped</div>
        <SlotCompo_64>
            <template v-slot:default="player">
                {{ player.member }}
            </template>
        </SlotCompo_64>
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