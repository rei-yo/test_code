<template>
    <div>
        <slot name = "header" />
        <nav>ここにナビゲーションバーを入れる default.vue</nav>
        <Navbar />
        <slot />
    </div>
</template>
<script setup></script>
<style>
  .page-enter-active,
  .page-leave-active {
    transition: all 0.4s;
  }
  .page-enter-from,
  .page-leave-to {
    opacity: 0;
    filter: blur(1rem);
  }
</style>