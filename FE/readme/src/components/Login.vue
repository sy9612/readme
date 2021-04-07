<template>
  <div id="Login">
    <label for="">아이디</label>
    <input type="text" v-model="credentials.username">
    <label for="">비밀번호</label>
    <input type="password" v-model="credentials.password">
    <button @click="login">로그인</button>
  </div>
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

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
          const usern = JSON.parse(res.config.data).username
          localStorage.setItem('username', usern)
          this.$emit('login', usern)
          this.$router.push({ name: 'Home' })
        })
    }
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
  color: white;
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
  }
</style>