<template>
  <div id="Signup">
    <div class="signup-input">
      <div class="left-input">
        <label for="#">아이디</label>
        <input type="text" v-model="params.username" @keypress.space="checkSpace" 
        onfocus="this.placeholder=''" onblur="this.placeholder='영문,숫자 / 12자 이내'" placeholder="영문,숫자 / 12자 이내">  
        <label for="#">비밀번호</label>
        <input type="password" v-model="params.password1" @keypress.space="checkSpace"
        onfocus="this.placeholder=''" onblur="this.placeholder='영문,숫자,특수기호 / 8자 이상'" placeholder="영문,숫자,특수기호 / 8자 이상">  
        <label for="#">비밀번호 확인</label>
        <input type="password" v-model="params.password2" @keypress.space="checkSpace"
        onfocus="this.placeholder=''" onblur="this.placeholder='영문,숫자,특수기호 / 8자 이상'" placeholder="영문,숫자,특수기호 / 8자 이상">  
        <label for="#">이메일</label>
        <input type="text" v-model="params.email" @keypress.space="checkSpace" 
        onfocus="this.placeholder=''" onblur="this.placeholder='이메일을 입력해주세요'" placeholder="이메일을 입력해주세요">  
      </div>
      
      <div class="right-input">
        <label for="#">닉네임</label>
        <input type="text" v-model="params.nickname" @keypress.space="checkSpace" 
        onfocus="this.placeholder=''" onblur="this.placeholder='10자 이내'" placeholder="10자 이내">  
        <label for="#">성별</label>
        <div class="radio-btn">
          <input type="radio" name="gender" value="남" v-model="params.gender">남
          <input type="radio" name="gender" value="여" v-model="params.gender">여
        </div>
        <label for="#">생년월일</label>
        <input type="date" v-model="params.birth">
        <label for="#">MBTI</label>
        <select name="mbti" v-model="params.mbti_id">
          <option value="1">ENTF</option>
          <option value="2">ENTJ</option>
          <option value="3">INTF</option>
          <option value="4">INTJ</option>
        </select>
      </div>
    </div>
    <b-button @click="signup" pill variant="outline-secondary">작성완료</b-button>
  </div>
  
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: "Signup",
  data: function () {
    return {
      params: {
        "email": "",
        "username": "",
        "password1": "",
        "password2": "",
        "nickname": "",
        "gender": "",
        "birth": "",
        "mbti_id": 0,
      },
    }
  },
  props: {
    menuIsOpen: Boolean
  },
  methods: {
    checkSpace: function() {
      event.returnValue = false;
    },
    signup: function () {
      let nullCheck = true
      let pwCheck = false
      // for (let key in this.params) {
      //     if (!this.params[key]) {
      //       nullCheck = false
      //     }
      // } 
      if (this.params.userPw === this.pwConfirm) {
        pwCheck = true
      }
      if (nullCheck && pwCheck) {
        axios.post(`${SERVER_URL}/accounts/signup`, this.params)
          .then(res => {
            alert('회원가입이 완료되었습니다!')
            this.$router.push({name: 'Login'})
          })
          .catch(err => {
            alert('회원정보를 확인해주세요!!')
          })
      }
    }
  },
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Signup')
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
    this.$emit('page','SignUp')
  }
}
</script>

<style>
  #Signup {
    position: absolute;
    left: 0;
    top: 0;
    box-sizing: border-box;
    padding-top: 13%;
    display: flex;
    align-items: center;
    flex-direction: column;
    /* width: 100%;
    height: 100%; */
    background: url(../assets/Book.jpg) no-repeat center center;
    background-size: 100vw 100vh;
    /* opacity: 0.5; */
    height: 100vh;
    width: 100vw;
    color: rgb(160, 133, 133);
    font-weight: bold;
  }
  #Signup label {
    margin-bottom: 3%;
    width: 50%;
    height: 7%;
  }
  .signup-input {
    display: flex;
    justify-content: space-between;
    /* align-items: ; */
    height: 65%;
    width: 30%;
  }
  input::placeholder {
    font-size: 70%;
  }
  .left-input {
    position: relative;
    height: 100%;
    width: 45%;
    display: flex;
    flex-direction: column;
    margin-right: 3%;
  }
  #Signup input {
    margin-bottom: 7%;
    background: none;
    border: none;
    border-bottom: 1px dashed white;
    font-size: 120%;
    outline: none;
    font-family: font1;
  }
  .right-input {
    position: relative;
    height: 100%;
    width: 45%;
    display: flex;
    flex-direction: column;
    /* margin-right: 3%; */
  }
  .radio-btn {
    margin-bottom: 3.2%;
  }
  .signup-btn {
    cursor: pointer;
  }
</style>