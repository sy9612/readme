<template>
  <div id="Login">
    <label for="">아이디</label>
    <input type="text" v-model="credentials.username" placeholder="아이디를 입력해주세요" onfocus="this.placeholder=''"
    onblur="this.placeholder='아이디를 입력해주세요'">
    <label for="">비밀번호</label>
    <input type="password" v-model="credentials.password" placeholder="영문,숫자,특수기호 / 8자 이상" onfocus="this.placeholder=''"
    onblur="this.placeholder='영문,숫자,특수기호 / 8자 이상'">
    <b-button @click="login" pill variant="outline-secondary">작성완료</b-button>
  </div>
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/login`, this.credentials)
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          console.log(res)
          const token = res.data['token']
          const decoded = jwt_decode(token)
          localStorage.setItem('user_id', decoded.user_id)
          const usern = JSON.parse(res.config.data).username
          localStorage.setItem('username', usern)
          this.$emit('login', usern)
          alert('로그인되었습니다!')
          this.$router.push({ name: 'Home' })
        })
        .catch(err=>{
            console.log(err)
            alert('로그인 정보를 확인해주세요!')
        })
    }
  },
  created: function () {
    this.$emit('page','Login')
    this.$emit('isHome', this.$route.name)
  }
}
</script>

<style>
#Login {
  position: absolute;
  left: 0;
  top: 0;
  box-sizing: border-box;
  padding-top: 14%;
  display: flex;
  align-items: center;
  flex-direction: column;
  /* width: 100%;
  height: 100%; */
  background: url(../assets/Book.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  /* opacity: 0.9; */
  height: 100vh;
  width: 100vw;
  color: rgb(160, 133, 133);
  font-weight: bold;
}
  #Login label {
    margin-bottom: 1%;
  }
  #Login input {
    margin-bottom: 4%;
    background: none;
    border: none;
    border-bottom: 1px dashed white;
    font-size: 120%;
    outline: none;
    font-family: font1;
    text-align: center;
  }
  #Login ::-webkit-input-placeholder {
    text-align: center;
  }
</style>