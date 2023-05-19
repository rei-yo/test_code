<script>
export default {
    props: {
    msg: String
    },

    emits: ["response"],
    created() {
        //emit(イベント名,データ）
        this.$emit('response', 'hello from child')
        }
}
</script>

<template>
    
    <h2>A Child Component!</h2>
    <!-- ||は論理和。msgがtrueならmsg,それ以外はNoを返す。-->
    <h2>{{ msg || 'No props passed yet' }}</h2>

    <slot>Fallback content</slot>

</template>