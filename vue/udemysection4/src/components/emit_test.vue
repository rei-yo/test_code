<script setup>

    const emitTest = defineEmits(['customEvent', 'customEvent2'])

    function childMethod() {
        emitTest('customEvent', '子の値', '子の値2')
        emitTest('customEvent2', '2')
    }

</script>

<template>

    <div>
        <button @click = "childMethod">子側のボタン</button>
        <button @click = "childMethod">count</button>
    </div>

</template>
