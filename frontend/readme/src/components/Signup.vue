<template>
  <div id="Signup">
    <div class="left-input">
      <label for="#">아이디</label>
      <input type="text" v-model="params.userId" @keypress.space="checkSpace" 
      onfocus="this.placeholder=''" onblur="this.placeholder='아이디를 입력해주세요!'" placeholder="아이디를 입력해주세요!">  
      <label for="#">비밀번호</label>
      <input type="password" v-model="params.userPw" @keypress.space="checkSpace"
      onfocus="this.placeholder=''" onblur="this.placeholder='비밀번호를 입력해주세요!'" placeholder="비밀번호를 입력해주세요!">  
      <label for="#">비밀번호 확인</label>
      <input type="password" v-model="pwConfirm" @keypress.space="checkSpace"
      onfocus="this.placeholder=''" onblur="this.placeholder='비밀번호를 한 번 더 입력해주세요!'" placeholder="비밀번호를 한 번 더 입력해주세요!">  
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

    </div>
  </div>
</template>

<script>
// const SERVER_URL = "dddd"

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
    checkSpace: function(){
        event.returnValue = false;
    },    
  }
}
</script>

<style>
  #Signup {
    position: absolute;
    display: flex;
    top: 30%;
    width: 50%;
    height: 50%;
  }
  #Signup label {
    margin-bottom: 3%;
  }
  .left-input {
    position: relative;
    height: 50%;
    width: 40%;
    display: flex;
    flex-direction: column;
    margin-right: 10%;
  }

  .left-input input {
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
    width: 50%;
    display: flex;
    flex-direction: column;
  }
</style>