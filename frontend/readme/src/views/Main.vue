<template>
  <div id="main">
    <div class="main-message">
      <div>도서 추천 서비스-README</div>
      <div>여러분의 독서고민</div>
      <div>우리가 해결해드려요</div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
#main {
  position: relative;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
  background: url(../assets/main.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  height: 100vh;
  width: 100vw;
  color: white;
  font-weight: bold;
}
.main-message {
  position: absolute;
  top: 43%;
  height: 40%;
  width: 30%;
  font-size: 150%;
}
.main-message div {
  margin-bottom: 5%;
}
.main-message div:nth-child(n+2) {
  font-size: 200%;
}
.main-message div:nth-child(3) {
  color: #2c3e50;
}
</style>