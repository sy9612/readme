<template>
  <div id="Report">
    <div class="report_wrapper">
      <div class="report_left">
        <div class="book_info">
          <img :src="imgsrc" alt="">
          <div class="book_contents">
            <p class="report_book_title" @click="toDetail">{{ bookinfo.book_title }}</p>
            <p>{{ bookinfo.book_author }}</p>
            <p>{{ maincategory }}</p>
            <p>{{ subcategory }}</p>
          </div>
        </div>
        <p>{{ bookinfo.book_description }}</p>
      </div>
      <div class="report_right">
        <textarea v-model="params.report_content" cols="10" rows="10"></textarea>
        <b-button @click="postReport" pill variant="outline-secondary">작성완료</b-button>
      </div>
    </div>
  </div>


</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'Report',
  data: function () {
    return {
      book_info: [],
      params: {
        book_isbn: 0,
        report_content: '',
      },
      imgsrc: '',
      bookinfo: {},
      maincategory: '',
      subcategory: '',
    }
  },
  props: {
    menuIsOpen: Boolean,
  },
  methods: {
    postReport: function () {
      const user_id = localStorage.getItem('user_id')
      axios.post(`${SERVER_URL}/reports/${user_id}`, this.params)
        .then((res) => {
          alert('작성되었습니다!')
        })
    },
    toDetail: function () {
      this.$router.push({name: 'Detail', params:{bookIsbn: this.bookinfo.book_isbn}})
    },
  },
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Report')
      if (this.menuIsOpen === false) {
          page.style.transform = 'scale(1)'
      } else {
        page.style.transform = 'scale(0)'
        page.style.transitionDuration = '0.4s'
        page.style.transitionTimingFunction = 'ease-out'
      }
    },
  },
  created: function () {
    const isbn = this.$route.params.bookIsbn
    this.params.user_id = localStorage.getItem('user_id')
    axios.get(`${SERVER_URL}/books/${isbn}`)
      .then(res => {
        this.bookinfo = res.data.book
        this.maincategory = res.data.maincategory
        this.subcategory = res.data.subcategory
        this.imgsrc = `http://j4a205.p.ssafy.io:8050/images/${this.bookinfo.book_isbn}.jpg`
      })  
    this.$emit('page','BookReport')
    this.$emit('isHome', this.$route.name)
  
  }
}
</script>

<style>
#Report {
  position: absolute;
  display: flex;
  flex-direction: column;
  background: url(../assets/background.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 22%;
  padding-top: 4.2%;
}
.report_left {
  /* height */
}
.report_wrapper {
  position: relative;
  display: flex;
  justify-content: space-between;
  margin-top: 10%;
  height: 86.9%;
  width: 100%;
  background: rgba(165, 142, 142, 0.5);
  border-radius: 20px;
  padding: 2%;
  opacity: 0.8;
}
.report_wrapper > div {
  position: relative;
  width: 49.8%;
  background: rgb(250, 248, 247);
  border-radius: 20px;
  padding: 1%;
  box-shadow: 5px 5px;
}
.book_info {
  position: relative;
  display: flex;
  justify-content: space-between;
  height: 50%;
  overflow: hidden;
}
.book_info img {
  height: 100%;
  width: 48%;
  /* border-radius: 10px; */
}
.book_contents {
  width: 48%;
}
.report_book_title:hover {
  opacity: 0.5;
  cursor: pointer;
}
.report_left > p {
  position: relative;
  box-sizing: border-box;
  padding: 1% 3%;
  height: 43%;
  overflow: auto;
}
.report_left > p::-webkit-scrollbar {
  display: none;
}
.report_right {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.report_right textarea {
  position: relative;
  font-family: font1;
  /* margin-top: 10%; */
  width: 100%;
  height: 90%;
  background: none;
  border: none;
  outline: none;
  background-attachment: local;
  background-image:
    linear-gradient(to right, rgb(250, 248, 247) 10px, transparent 10px),
    linear-gradient(to left, rgb(250, 248, 247) 10px, transparent 10px),
    repeating-linear-gradient(rgb(250, 248, 247), rgb(250, 248, 247) 30px, #ccc 30px, #ccc 31px, rgb(250, 248, 247) 31px);
  line-height: 31px;
  margin-bottom: 2%;
}
.report_right button {
  /* width: 17%; */
}
</style>