<template>
  <div>
    <NuxtLayout :name = "layout">
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
  const admin = true;
  const layout = admin ? 'custom' : 'default';
</script>