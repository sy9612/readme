<template>
  <div id="Report">
    <div class="report_wrapper">
      <div class="report_left">
        <div class="book_info">
          <img src="../assets/harry.jpg" alt="">
          <div class="book_contents">
            <p>해리포터와 마법사의 돌</p>
            <p>장르: 공포</p>
            <p>상세내용: Lorem ipsum dolor sit amet consectetur, adipisicing elit. Qui, doloribus.</p>
          </div>
        </div>
      </div>
      <div class="report_right">
        <textarea v-model="params.report_content" cols="10" rows="10"></textarea>
        <button @click="postReport">작성완료</button>
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
      }
      
    }
  },
  methods: {
    postReport: function () {
      
      const user_id = localStorage.getItem('user_id')
      axios.post(`${SERVER_URL}/reports/${user_id}/`, this.params)
    }
  },
  created: function () {
    this.params.book_isbn = this.$route.params.bookIsbn
    // const bookId = this.$route.params.bookId
    // axios.get(`${SERVER_URL}/market/detail/${bookId}/`) 
    //   .then((res) => {
    //     this.book_info = res.data
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })

   
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
  padding-top: 7%;
}
.report_wrapper {
  position: relative;
  display: flex;
  justify-content: space-between;
  margin-top: 10%;
  height: 100%;
  width: 100%;
  background: rgb(166, 180, 177);
  border-radius: 20px;
  padding: 2%;
}
.report_wrapper > div {
  position: relative;
  width: 49.8%;
  background: rgb(191, 201, 200);
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
    linear-gradient(to right, rgb(191, 201, 200) 10px, transparent 10px),
    linear-gradient(to left, rgb(191, 201, 200) 10px, transparent 10px),
    repeating-linear-gradient(rgb(191, 201, 200), rgb(191, 201, 200) 30px, #ccc 30px, #ccc 31px, rgb(191, 201, 200) 31px);
  line-height: 31px;
  margin-bottom: 2%;
}
</style>