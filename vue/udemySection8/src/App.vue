<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import Header from './global/Header.vue'
import BookSearch from './pages/BookSearch.vue';

const router = useRouter()
const STORAGE_KEY = 'books'
const books = ref([])

// getItemでデータを確認し、データがあればbookに定義し、無ければデータがおかしいので削除する。

onMounted(() => {
  if (localStorage.getItem(STORAGE_KEY)){
    try{
      books.value = JSON.parse(localStorage.getItem(STRAGE_KEY))
    } catch(e){
      localStorage.removeItem(STORAGE_KEY)
    }
  }
})

function addBook(e) {
  books.value.push({
    id: books.value.length,
    title: e.title,
    image: e.image,
    description: e.description,
    readDate: '',
    memo: ''
  })

  // booksにはlocalstorageに保管されてる全てのbookがある。
  // 追加したbookのidを取得したいので[-1]で最後のbookを指定
  saveBooks()
  console.log('savebooks',books.value.slice(-1)[0].id)
  goToEditPage(books.value.slice(-1)[0].id)
}

function saveBooks() {
  const parsed = JSON.stringify(books.value)
  localStorage.setItem(STORAGE_KEY, parsed)
}

function goToEditPage(id){
  router.push(`/edit/${id}`)
}

function updateBookInfo(e){
  const updateInfo = {
    id: e.id,
    readDate: e.readDate,
    memo: e.memo,
    title: books.value[e.id].title,
    image: books.value[e.id].image,
    description: books.value[e.id].description
  }
  books.value.splice(e.id, 1, updateInfo)
  saveBooks()
  router.push('/')
}



</script>

<template>
  <v-app>
    <Header />
    <v-main>
      <!-- v-container??? -->
      <RouterView
      :books = "books"
      @add-book-list = "addBook"
      @update-book-info ="updateBookInfo"
      />
    </v-main>
  <div>book:{{ books }}</div>
</v-app>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
