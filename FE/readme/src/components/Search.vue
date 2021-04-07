<template>
  <div id="Search">
    <div class="search-bar">
      <i class="fas fa-search"></i>
      <input @keypress.enter="search" v-model="content" type="text" class="search-input">
        <select name="option" v-model="searchCategory">
          <option value="all" selected>전체</option>
          <option value="title">제목</option>
          <option value="author">저자</option>
          <option value="description">내용</option>
        </select>
    </div>
    <img class="book-img" :src="results[0] + '.jpg'" alt="">
    
  </div>
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'Search',
  data: function () {
    return {
      searchCategory: '',
      content: '',
      results: [[9788999718298]],
    }
  },
  props: {
    menuIsOpen: Boolean,
  },
  methods: {
    search: function () {
      axios.get(`${SERVER_URL}/books/search?keyword=${this.content}&search_type=${this.searchCategory}`)
        .then(res => {
            this.results = res.data.books
            console.log(this.results)
        })
    }
  },
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Search')
      if (this.menuIsOpen === false) {
          page.style.display = 'flex'
      } else {
        page.style.display = 'none'
        // page.style.transitionDuration = '10s'
        page.style.transitionTimingFunction = 'ease-out'
      }
    },
  },
}
</script>

<style>
#Search {
  position: absolute;
  display: flex;
  flex-direction: column;
  background: #d7b9a1;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 32%;
  padding-top: 10%;
}
.search-bar {
  position: relative;
  padding-left: 3%;
  top: 20%;
  height: 43px;
  border: 1px solid gray;
  border-radius: 24px;
  box-shadow: 2px 2px 2px 2px;
  outline: none;
}
/* .search-bar:hover {
  
} */
.search-input {
  position: relative;
  height: 94%;
  width: 70%;
  background: none;
  border: none;
  outline: none;
  border-radius: 24px;
  margin-left: 2%;
}
.book-img {
  width: 30px;
  height: 30px;
}
</style>