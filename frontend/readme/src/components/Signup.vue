<template>
  <div id="Signup">
    <div class="left-input">
      <label for="#">아이디</label>
      <input type="text" v-model="params.userId" @keypress.space="checkSpace" 
      onfocus="this.placeholder=''" onblur="this.placeholder='영문,숫자 / 10자 이내'" placeholder="영문,숫자 / 10자 이내">  
      <label for="#">비밀번호</label>
      <input type="password" v-model="params.userPw" @keypress.space="checkSpace"
      onfocus="this.placeholder=''" onblur="this.placeholder='영문,숫자,특수기호 / 12자 이내'" placeholder="영문,숫자,특수기호 / 12자 이내">  
      <label for="#">비밀번호 확인</label>
      <input type="password" v-model="pwConfirm" @keypress.space="checkSpace"
      onfocus="this.placeholder=''" onblur="this.placeholder='영문,숫자,특수기호 / 12자 이내'" placeholder="영문,숫자,특수기호 / 12자 이내">  
      <label for="#">이메일</label>
      <input type="text" v-model="params.userEmail" @keypress.space="checkSpace" 
      onfocus="this.placeholder=''" onblur="this.placeholder='이메일을 입력해주세요'" placeholder="이메일을 입력해주세요">  
    </div>
    <div class="right-input">
      <label for="#">성별</label>
      <div>
        <input type="radio" name="gender" value="man" v-model="params.userGender">남
        <input type="radio" name="gender" value="woman" v-model="params.userGender">여
      </div>
      <label for="">나이</label>
      <input type="number" min="1" max="99" maxlength="2">
    </div>
  </div>
  <div class="signup-btn" @click="signup">SignUp</div>
</template>

<script>
const SERVER_URL = "dddd"
import axios from 'axios'

export default {
  name: "Signup",
  data: function () {
    return {
      params: {
        "userEmail": "",
        "userId": "",
        "userName": "",
        "userNick": "",
        "userPw": "",
        "userGender": "",
      },
      pwConfirm: "",
    }
  },
  methods: {
    checkSpace: function() {
      event.returnValue = false;
    },
    signup: function () {
      let nullCheck = true
      let pwCheck = false
      for (let key in this.params) {
          if (!this.params[key]) {
            nullCheck = false
          }
      } 
      if (this.params.userPw === this.pwConfirm) {
        pwCheck = true
      }
      if (nullCheck && pwCheck) {
        axios.post(`${SERVER_URL}/user/sign/id/${this.params.userId}`)
          .then( {

          })
      }
    }
  }
}
</script>

<style>
  #Signup {
    position: relative;
    display: flex;
    margin-top: 14%;
    width: 40%;
    height: 45%;
  }
  #Signup label {
    margin-bottom: 3%;
  }
  .left-input {
    position: relative;
    height: 50%;
    width: 47%;
    display: flex;
    flex-direction: column;
    margin-right: 3%;
  }

  #Signup input {
    margin-bottom: 8%;
    background: none;
    border: none;
    border-bottom: 1px dashed white;
    font-size: 120%;
    outline: none;
  }
  .right-input {
    position: relative;
    height: 50%;
    width: 47%;
    display: flex;
    flex-direction: column;
    margin-right: 3%;
  }
  .right-input {
    font-size: 110%;
  }
  .signup-btn {
    cursor: pointer;
  }
</style>