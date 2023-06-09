<script setup>

    import { reactive, computed } from "vue"

    const contact = reactive({
        yourName : "",
        tel : "",
        email : "",
        gender : "",
        age : "",
        message:"",
        attracts: [],
        caution : false
        })

    const errors = reactive([])
    const hasError = reactive({ yourName: false })

    function validate() {
        errors.splice(0)
    
        if(!contact.yourName){
            errors.push("氏名を入力してください")
            }else if(contact.yourName.length > 20){
            error.puth("氏名は20文字以下")
            }

        if (!contact.gender) {
            errors.push('性別を選択してください')
            }

        if(!contact.caution){
            errors.push("注意事項に同意してください")
        }

        if(!errors.length){
            console.log("送信可能")
        }
    }

    const yourName = computed({
    get() {
        return contact.yourName
    },
    set(newValue) {
        
        if (newValue.length<=20) {
            hasError.yourName = false
        } else {
            hasError.yourName = true
        }
        contact.yourName = newValue
    }
    })



</script>

<style scoped>
    [v-cloak]{
        display:none;
    }
    .error{
        color:red;
    }

</style>

<template>
    <div>
        <div v-if="errors.length" v-for="error in errors" class="error">
            {{error}}
        </div>
    </div>
    <form @submit.prevent="validate">
        氏名
        <input type="text" v-model = "contact.yourName" placeholder = "your name">
        <br>
        <span :class="{error: hasError.yourName}">{{ contact.yourName.length }} /20</span>
        <br>
        <div v-show="hasError.yourName" class="error">氏名は20文字以下で記入</div>
        電話番号
        <input type="tel" v-model.number="contact.tel">
        <br>
        メールアドレス
        <input type="email" v-model.lazy.trim="contact.email">
        <br>
        性別
        <input type="radio" value="male" v-model="contact.gender">男性
        <input type="radio" value="female" v-model="contact.gender">女性
        <br>
        年齢
        <select v-model="contact.age">
            <option disabled value="">年齢を選択してください</option>
            <option>10代</option>
            <option>20代</option>
            <option>30代</option>
            <option>40代</option>
            <option>50代～</option>
        </select>
        <br>
        メッセージ
        <textarea v-model="contact.message"></textarea>
        <br>
        このサイトを知った理由
        <input type="checkbox" value="webサイト" v-model="contact.attracts">webサイト
        <input type="checkbox" value="チラシ" v-model="contact.attracts">チラシ
        <input type="checkbox" value="その他" v-model="contact.attracts">その他
        <br>
        注意事項に同意する
        <input type="checkbox" v-model="contact.caution">
        <br>
        <input type="submit" value="送信">
    </form>
</template>