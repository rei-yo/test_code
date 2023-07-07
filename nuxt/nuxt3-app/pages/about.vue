<template>
    <div>
      <NuxtLayout>
        <h1>About Page</h1>
      </NuxtLayout>
    </div>
  </template>

<script setup>
//   definePageMeta({
//     layout: 'custom',
//   });
    definePageMeta({
        layout: false,
        middleware: 'auth',
    });
</script>