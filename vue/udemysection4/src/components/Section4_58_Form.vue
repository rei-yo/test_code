<script setup>

    const props = defineProps(["value"])
    const emit = defineEmits(["update:value"])

    function childEvent(e) {
        console.log("emit from CustomInput_58", e.target.value)
        emit("update:value", e.target.value)
    }

</script>

<template>
    <div>
    <!-- valueはpropsで親から受け取ったデータ @inputがv-on省略形 -->
        <input :value = "value" @input = "childEvent">
    </div>

</template>