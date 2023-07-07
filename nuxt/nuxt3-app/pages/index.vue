<template>
    <div>
        <h1>Main Page from index</h1>
        <NuxtLayout name="default">
            <template #header>ヘッダー</template>
            <button @click="enableCustomLayout">Update layout</button>
        </NuxtLayout>
        <button @click="handleClick">Coupon Get</button>
        <LazyCoupon v-if="show" />
        <img src="~/assets/icon.png" alt="Nuxt3 Icon" />

        <div>
            <div>Count: {{ count }}</div>
            <button @click ="() => inc()">increase</button>
            <button @click = "() => dec()">decrease</button>
        </div>
    </div>
</template>

<script setup>
definePageMeta({
layout: false,
});

function enableCustomLayout(){
setPageLayout('custom');
}

const show = ref(false);
const handleClick = () => {
show.value = true;
}

const { count, inc, dec } = useCounter(100);
</script>