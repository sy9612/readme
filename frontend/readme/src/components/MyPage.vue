<template>
  <div id="MyPage">
    <div class="mypage-list">
      <span>찜 목록</span>
      <span>읽는 중</span>
      <span>다 읽은 책</span>
      <span>책 쌓기</span>
      <button @click="clickBtn">누르면 1번 책 세부</button>
      <button @click="clickDib">누르면 책 찜</button>
      <div v-if="clickedDib">찜했다!</div>
      <div v-else>찜 안했다!</div>
      <button @click="clickMyList">내찜리스트</button>
    </div>
  </div>
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'MyPage',
  data: function () {
    return {
      clickedDib:false,
    }
  },
  created: function () {
    const config = this.setToken()
    axios.get(`${SERVER_URL}/books/list`,config)
      .then(res => {
        console.log(res)
      })
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },

    clickBtn: function(){
      const config = this.setToken()
      axios.get(`${SERVER_URL}/books/700`,config)
      .then(({data}) => {
        console.log(data)
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    clickMyList: function(){
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/dibsList`,config)
      .then(({data}) => {
        console.log(data)
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    clickDib: function(){
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/clickDibs/700`,config)
      .then(({data}) => {
        this.clickedDib=data.dibSelect
      })
      .catch( (err) => {
        console.log(err)
      })
    }
  }
}   
</script>

<style>
#MyPage {
  position: absolute;
  background: #d7b9a1;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 20%;
  padding-top: 10%;
}
.mypage-list {
  /* border: 2px solid red; */
}
.mypage-list span {
  margin-right: 5%;
}
.mypage-list span:nth-child(1) {
  font-weight: bold;
  font-size: 115%;
}
</style>