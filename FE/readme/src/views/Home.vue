<template>
  <div id="Home">
    <div class="scroll">
      <div>up</div>
      <div @click="nextMainPage">down</div>
    </div>
    <div class="home-message">
      <div>도서 추천 서비스 - README</div>
      <div>여러분의 독서고민</div>
      <div>우리가 해결해드려요</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data: function () {
    return {};
  },
  components: {},
  props: {
    menuIsOpen: Boolean,
  },
  methods: {},
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Home');
      if (this.menuIsOpen === false) {
        page.style.display = 'flex';
      } else {
        page.style.display = 'none';
        // page.style.transitionDuration = '10s'
        page.style.transitionTimingFunction = 'ease-out';
      }
    },
  },
};
</script>

<style>
#Home {
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  align-items: center;
  flex-direction: column;
  /* width: 100%;
  height: 100%; */
  background: url(../assets/main.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  height: 100vh;
  width: 100vw;
  color: white;
  font-weight: bold;
}
.scroll {
  position: absolute;
  top: 80%;
}
.home-message {
  position: absolute;
  top: 34%;
  height: 40%;
  width: 30%;
  font-size: 150%;
}
.home-message div {
  margin-bottom: 3%;
}
.home-message div:nth-child(1) {
  font-size: 50%;
}
.home-message div:nth-child(n + 2) {
  font-size: 200%;
}
.home-message div:nth-child(3) {
  color: #2c3e50;
}
</style>
