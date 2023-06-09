<script setup>

    import { computed } from "vue"

    const props = defineProps(["value"])
    const emit = defineEmits(["customEvent"])

    const value = computed({
        //getは表示する方
        get() {
            console.log("emit from CustomInput_59", props.value)
            return props.value
        },
        set(value){
            emit("customEvent", value)
        }
    
    })

</script>

<template>
    <div>
        <input :value = "value">
    </div>

</template>