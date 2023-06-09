

<script setup>

</script>

<template>
    <div>
        <div>
            <slot name="header">child header</slot>
        </div>
        <div>
            <slot>child main contents</slot>
        </div>
        <div>
            <slot name = "footer">child footer</slot>
        </div>
    </div>

</template>