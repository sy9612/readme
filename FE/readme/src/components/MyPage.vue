<<<<<<< HEAD
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
=======

<template>

  <div id = "MyPage">
    <a @click="wishMethod" :style="wishstyle" style="cursor:pointer; margin-right: 15px; font-size: 30px">찜한 도서</a>
    <a @click="readMethod" :style="readstyle" style="cursor:pointer; font-size: 30px">읽은 도서</a>

    <div v-if="wish"><wish-list></wish-list></div>
    <div v-if="read"><read-list></read-list></div>
  </div>

  
</template>

<script>
import WishList from './WishList.vue'
import ReadList from './ReadList.vue'

export default {
  name: 'MyPage',
  components: { WishList, ReadList },
  data: function(){
    return{
      wishstyle:{
        textDecoration: 'underline',
      },
      readstyle:{
        textDecoration: '',
      },
      wish: true,
      read: false,
    };
  },
  
  methods: {
  	wishMethod:function() {
      this.wish = true
      this.read = false
      this.readstyle.textDecoration = ''
      this.wishstyle.textDecoration = 'underline'


    },
    readMethod: function(){
      this.wish = false
      this.read = true
      this.readstyle.textDecoration = 'underline'
      this.wishstyle.textDecoration = ''
    },
  }
  
}

>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
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
<<<<<<< HEAD
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
=======
  padding: 0 10%;
  padding-top: 10%;
}

</style>
>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
