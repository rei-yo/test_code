<script>
    export default {
        data() {
            return {
                message: 'Hello World!',
                awesome: true, //toggleでtrue, falseの切り替え

                counter: {
                    count: 0
                    }, //オブジェクト的な書き方
                    
                todos: [
                    { id: id++, text: 'Learn HTML' },
                    { id: id++, text: 'Learn JavaScript' },
                    { id: id++, text: 'Learn Vue' }
                    ]
                }
            },
        //メソッドを定義。
        methods: {
            increment() {
                //メソッドを定義。thisを使用してコンポーネントインスタンスにアクセス
                this.counter.count++
                },

            //メソッドに引数を記述。v-onハンドラーはネイティブDOMのイベントが入る
            onInput(e){
                this.text = e.target.value
                },

            toggle() {
                this.awesome = !this.awesome
                }
            }
    }
</script>

<template>
    <h1>{{ message }}</h1>

    <div>Count is: {{ counter.count }}</div>

    <!--v-onでDOMイベントのサブスク（イベントリスナー）。省略記法で記載 -->
    <button @click="increment">count up</button>

    <!-- 属性バインディング。v-bind:id='xxx'が正式 -->
    <div :class='title'>
        <h1>Make me red</h1>
    </div>

    <!-- v-bind と v-on を一緒に使うことで、input 要素に双方向 (two-way) バインディング -->
    <input :value='text' @input="onInput">
    <div> {{ text }}</div>

    <!-- ifを使って条件付きレンダリング awesomeがtrueのときにifが実行-->
    <button @click ="toggle"> awesome </button>
    <h1 v-if="awesome"> Vue is awesome!</h1>
    <h1 v-else> Oh no T_T</h1>

    <!-- for-->
    <ul>
        <li v-for = "todo in todos" :key = "todo.id">
            {{ todo.text }}
        </li>
    </ul>

</template>

<style>
    .title {
        color:red;
        }
</style>