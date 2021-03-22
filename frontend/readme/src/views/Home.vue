<template>
  <div id="home">
    <div class="menu">
      <div class="page-name">MENU</div>
      <div class="menu-list">
        <div>독서 현황</div>
        <div>독서 현황</div>
        <div>독서 현황</div>
        <div>독서 현황</div>
      </div> 
    </div>
    <div class="main">
      <div class="main-title">
        <span>README</span>
        <button @click="clickMenu">MENU</button> 
      </div>
    </div>
    <Main />
  </div>
</template>

<script>
import Main from '@/views/Main'

export default {
  name: 'Home',
  components: {
    Main,
  },
  methods: {
    clickMenu: function () {
      
    }
  },
  watch: function () {

  }
}
</script>

<style>
#home {
  position: absolute;
  height: 100%;
  width: 100%;
  /* z-index: 0; */
}
.menu {
  position: absolute;
  box-sizing: border-box;
  padding: 0 10%;
  padding-top: 5%;
  height: 100%;
  width: 100%;
  z-index: 2;
  background: #d7b9a1;
}
.main {
  position: absolute;
  height: 100%;
  width: 100%;
}
.main-title {
  position: absolute;
  display: flex;
  justify-content: space-between;
  overflow: hidden;
  /* left: 10%; */
  padding: 0 10%;
  top: 10%;
  height: 6%;
  width: 80%;
  font-size: 2.5rem;
  z-index: 3;
}
.page-name {
  position: relative;
  width: 70%;
  left: 30%;
}
.menu-list {
  position: relative;
  left: 20%;
  top: 10%;
  width: 80%;
  font-size: 2.5rem;
  font-weight: bold;
}
.menu-list > div {
  margin-bottom: 2%;
}
</style>
