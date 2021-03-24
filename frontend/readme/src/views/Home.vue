<template>

  <div class="menu">
    <div class="menu-list">
      <div @click="toSearch">Search</div>
      <div @click="toReport">Book Report</div>
      <div>Recommendations</div>
      <div>My Page</div>
    </div> 
  </div>
  <div class="basic">
    <div class="main-title">
      <span class="project-name">README <span class="page-name">PageName</span> </span>
      <button @click="clickMenu">MENU</button> 
    </div>
    <div class="account">
        <span class="logout-btn">logout</span>
        <span class="signup-btn" @click="clickSignup">signup</span>
        <span>login</span>
    </div>
  </div>
  <Main :mainIsOpen='mainIsOpen' :signupIsOpen='signupIsOpen' />
</template>

<script>
import Main from '@/views/Main'

export default {
  name: 'Home',
  data: function () {
    return {
      mainIsOpen: true,
      signupIsOpen: false,
    }
  },
  components: {
    Main,
  },
  methods: {
    clickMenu: function () {
      this.mainIsOpen = !this.mainIsOpen
    },
    toSearch: function () {
      
    },
    clickSignup: function () {
      this.signupIsOpen = !this.signupIsOpen
    },
  },
  watch: function () {

  }
}
</script>

<style>
.menu {
  position: absolute;
  box-sizing: border-box;
  padding: 0 10%;
  padding-top: 5%;
  height: 100%;
  width: 100%;
  /* z-index: 1; */
  background: #d7b9a1;
}
.basic {
  position: absolute;
  box-sizing: border-box;
  height: 100%;
  width: 100%;
  padding: 6% 10%;
}
.main-title {
  position: relative;
  display: flex;
  justify-content: space-between;
  overflow: hidden;
  /* left: 10%; */
  /* padding: 0 10%; */
  /* margin-top: 6.5%; */
  height: 8%;
  /* width: 80%; */
  font-size: 2.5rem;
  z-index: 3;
  color: white;
}
.project-name {
  width: 60%;
}
.page-name {
  position: absolute;
  margin-left: 8%;
  font-size: 50%;
  height: 100%;
  top: 0;
}
.account {
  position: relative;
  /* display: flex; */
  height: 150px;
  width: 150px;
  padding-left: 0;
  transform: rotate(-90deg);
  transform-origin: center;
  /* flex-direction: column; */
  color: white;
  z-index: 3;
}
.account > span {
  position: relative;
  right: 0;
  transform: rotate(90deg);
  transform-origin: top right;
  margin-right: 12%;
  font-size: 130%;
  cursor: pointer;
}
.login-btn {
  margin-top: 10%;
}
.logout-btn {
  display: none;
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
