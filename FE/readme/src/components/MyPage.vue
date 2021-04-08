
<template>

  <div id = "MyPage">
    <div v-if="this.jwt == null">
      로그인 후 이용하실 수 있습니다.
    </div>
    <div v-else>
    <a @click="wishMethod" :style="wishstyle" style="cursor:pointer; margin-right: 15px; font-size: 30px">찜한 도서</a>
    <a @click="readMethod" :style="readstyle" style="cursor:pointer; font-size: 30px">읽은 도서</a>

    <div v-if="wish"><wish-list></wish-list></div>
    <div v-if="read"><read-list></read-list></div>
    </div>
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
  created() {
    this.fnGetUsr();
  },
  methods: {
    fnGetUsr: function () {
      const jwt = localStorage.getItem('jwt');
      const user_id = localStorage.getItem('user_id');
      const user_name = localStorage.getItem('username');
      this.user_id = user_id;
      this.user_name = user_name;
      this.jwt = jwt;
      // console.log(jwt);
      console.log(this.user_name);
    },
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

</script>

<style>
#MyPage {
  position: absolute;
background: url(../assets/background.jpg) no-repeat center center;
  background-size: 100% 100%;
    box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 10%;
  padding-top: 10%;
}

</style>
