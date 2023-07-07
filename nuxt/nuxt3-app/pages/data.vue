<script setup>
  const { data : users} = await useFetch(
    // 'https://jsonplaceholder.typicode.com/posts/'
    'http://127.0.0.1:8000/get_user'
  );

  console.log(users)

</script>
<template>
  <div>
    <h1>Posts一覧</h1>
    <ul>
      <li v-for="user in users.userdata" :key="user.userid">
        id:{{ user.userid }} name: {{user.username }}
      </li>
    </ul>
  </div>
</template>