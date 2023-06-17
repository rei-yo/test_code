<script setup>
    import { defineProps } from 'vue'
    import { ref, reactive } from 'vue'

    const props = defineProps({
        id: Number,
        title: String,
        content: String,
    })

// import { useRoute } from 'vue-router';

// const id = ref(null);
// const title = ref(null);
// const content = ref(null);

// const route = useRoute();

// id.value = route.params.id;
// title.value = route.query.title;
// content.value = route.query.content;

const books = reactive([
  {id:1, title:'タイトル1', content:'本の内容１'},
  {id:2, title:'タイトル2', content:'本の内容２'},
  {id:3, title:'タイトル3', content:'本の内容３'},
])
const bookIndex = ref(props.id - 1)
const illegalIndex = ref(bookIndex.value > books.length)
const book = ref( illegalIndex.value ? {} : books[bookIndex.value])


if ( illegalIndex.value ) {
  router.push('/book')
}


</script>

<template>

    <div>
        <p>本の詳細</p>
        <p>id:{{ id  }}</p>
        <p>タイトル：{{ book.title }}</p>
        <p>本の内容：{{ book.content }}</p>

    </div>

</template>