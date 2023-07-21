<template>
    <div>
        <nav>
            <NuxtLink to="/">Home</NuxtLink><span>&nbsp&nbsp</span>
            <NuxtLink to="/about">About</NuxtLink><span>&nbsp&nbsp</span>
            <NuxtLink to="https://google.com">google</NuxtLink><span>&nbsp&nbsp</span>
            <NuxtLink :to="{ name: 'users-list' }">User List</NuxtLink><span>&nbsp&nbsp</span>
            <NuxtLink to="/data">data</NuxtLink>
        </nav>
    </div>
</template>