<template>
  <div id="Login">
    <label for="">아이디</label>
    <input type="text">
    <label for="">비밀번호</label>
    <input type="password">
  </div>
</template>

<script>
export default {
  name: 'login',
  
}
</script>

<style>
#Login {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 14%;
  width: 40%;
  height: 45%;
}
  #Login label {
    margin-bottom: 3%;
  }
  #Login input {
    margin-bottom: 8%;
    background: none;
    border: none;
    border-bottom: 1px dashed white;
    font-size: 120%;
    outline: none;
  }
</style>