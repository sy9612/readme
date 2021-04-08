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

    <div class="search_result">
      <div v-for="(result, idx) in results" :key="idx" @click="toResultDetail(result.book_isbn)" class="result_card">
        <img :src="`http://j4a205.p.ssafy.io:8050/images/${result.book_isbn}.jpg`" alt="">
        <p></p>
      </div>
    </div>
    
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
      results: {},
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
    },
    toResultDetail: function(isbn) {
      this.$router.push({name: 'Detail', params:{bookIsbn:isbn}})
    },
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
  created: function () {
    this.$emit('page','Search')
  }
}
</script>

<style>
#Search {
  position: absolute;
  display: flex;
  align-items: center;
  flex-direction: column;
  background: url(../assets/background.jpg) no-repeat center center;
  background-size: 100% 100%;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 24%;
  padding-top: 12%;
}
.search-bar {
  position: relative;
  padding-left: 3%;
  width: 75%;
  /* top: 20%; */
  height: 43px;
  border: 1px solid gray;
  border-radius: 24px;
  box-shadow: 2px 2px 2px 2px;
  outline: none;
  margin-bottom: 6%;
}
.search-input {
  position: relative;
  height: 94%;
  width: 70%;
  background: none;
  border: none;
  outline: none;
  border-radius: 24px;
  margin-left: 2%;
  font-size: 120%;
  font-family: font1;
}
.search_result {
  position: relative;
  display: flex;
  /* justify-content: space-between; */
  height: 100%;
  width: 100%;
  overflow: auto;
  margin: 0 10%;
  flex-wrap: wrap;
}
.search_result::-webkit-scrollbar {
  display: none;
}
.search_result img {
  position: relative;
  width: 100%;
  height: 100%;
}
.result_card {
  position: relative;
  height: 50%;
  width: 18%;
  background-color: #fff;
  margin: 0 1%;
  margin-bottom: 5%;
  cursor: pointer;
}
.result_card:hover {
  opacity: 0.7;
}
</style>