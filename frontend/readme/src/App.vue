<template>
  <div id="App">
    <div class="navbar">
      <span> <span @click="toHome" class="project-name">README</span> <span class="page-name">PageName</span> </span>
      <button @click="clickMenu">MENU</button> 
    </div>

    <div class="account">
      <span v-if="login" class="logout-btn" @click="logout">logout</span>
      <span v-if="!login" class="signup-btn" @click="clickSignup">signup</span>
      <span v-if="!login" @click="clickLogin">login</span>
    </div>

    <div class="menu-list">
      <div @click="toSearch">Search</div>
      <div @click="toReport">Book Report</div>
      <div>Recommendations</div>
      <div>My Page</div>
    </div> 
  </div>

  <router-view :menuIsOpen="menuIsOpen" @login="logined" />
</template>

<script>
// import Main from '@/views/Main'

export default {
  name: 'App',
  data: function () {
    return {
      menuIsOpen: true,
      login: false,
    }
  },
  components: {
    // Main,
  },
  methods: {
    clickMenu: function () {
      this.menuIsOpen = !this.menuIsOpen
    },
    toSearch: function () {
      
    },
    clickSignup: function () {
      this.$router.push({name: 'Signup'})
    },
    clickLogin: function () {
      this.$router.push({name: 'Login'})
    },
    logout: function () {
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      this.login = false
      this.$router.push({name: 'Home'})
    },
    toHome: function () {
      this.$router.push({name: 'Home'})
    },
    logined: function () {
      this.login  = true
    }
  },
  watch: function () {

  }
}
</script>

<style>
#app {
  /* position: absolute; */
  box-sizing: border-box;
  padding: 0 5%;
  padding-top: 3%;
  height: 100vh;
  width: 100vw;
  /* z-index: 1; */
  background: #d7b9a1;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
.navbar {
  position: relative;
  display: flex;
  justify-content: space-between;
  overflow: hidden;
  height: 8%;
  font-size: 2.5rem;
  z-index: 3;
  color: white;
}
.navbar > span {
  width: 60%;
}
.project-name {
  cursor: pointer;
}
.page-name {
  position: absolute;
  margin-left: 16%;
  font-size: 33%;
  font-weight: bold;
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
  /* display: none; */
}
.menu-list {
  position: absolute;
  left: 30%;
  top: 17%;
  width: 50%;
  font-size: 2.5rem;
  font-weight: bold;
}
.menu-list > div {
  margin-bottom: 2%;
}
</style>
