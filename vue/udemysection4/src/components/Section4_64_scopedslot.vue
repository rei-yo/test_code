<script setup>

    import { ref } from 'vue'

    const member = ref({ name: "堂安", height : 170})

</script>

<template>
    <div>
        <div>
            <slot :member="member">child</slot>
        </div>
    </div>

</template>