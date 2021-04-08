<template>
  <div id="App">
    <div class="navbar">
      <span> <span @click="toHome" class="project-name">README</span> <span class="page-name">{{ pagename }}</span> </span>
      <div @click="clickMenu"><i class="menu-icon fas fa-bars"></i></div> 
    </div>

    <div class="account">
      <span v-if="login" class="logout-btn" @click="logout">logout</span>
      <span v-if="!login" class="signup-btn" @click="clickSignup">signup</span>
      <span v-if="!login" @click="clickLogin">login</span>
    </div>

    <div class="menu-list">
      <div @click="toSearch">Search</div>
      <div @click="toReport">Book Report</div>
      <div @click="toRecommendations">Recommendations</div>
      <div @click="toMyPage">My Page</div>
      <div @click="toDetail">Detail</div>
    </div> 
     <router-view :menuIsOpen="menuIsOpen" :onMenu="onMenu" @login="logined" @page="page" />
  </div>

 
</template>

<script >

// import Main from '@/views/Main'

export default {
  name: 'App',
  data: function () {
    return {
      menuIsOpen: true,
      login: false,
      onMenu: false,
      pagename: '',
      pageOrigin: '',
    }
  },
  components: {
    // Main,
  },
  methods: {
    clickMenu: function () {
      this.menuIsOpen = !this.menuIsOpen
      if (this.menuIsOpen===true) {
        this.pagename = 'Menu'
      } else {
        this.pagename = this.pageOrigin
      }
      
    },
    toSearch: function () {
      this.$router.push({name: 'Search'})
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
      localStorage.removeItem('user_id')
      this.login = false
      this.$router.push({name: 'Home'})
    },
    toHome: function () {
      this.$router.push({name: 'Home'})
    },
    toReport: function () {
      this.$router.push({name: 'Report', params:{bookIsbn:9788950992460}})
    },
    toMyPage: function () {
      this.$router.push({name: 'MyPage'})
    },
    toDetail: function () {
      this.$router.push({name: 'Detail', params:{bookIsbn:9788950992460}})
    },
    toRecommendations: function () {
      this.$router.push({name: 'Recommendations'})
    },
    logined: function () {
      this.login  = true
    },
    hoverMenu: function () {
      this.onMenu = !this.onMenu
    },
    page: function (page) {
      this.pagename = page
      this.pageOrigin = page
    }
  },
  created: function () {
    // const account = document.getElementsByClassName('account')
    // account.style.animation = 'fadein'
  },
  // watch: function () {

  // }
}
</script>

<style>
@font-face {
    font-family: font1;
    src: url(./fonts/font1.ttf) format('truetype');
}

@keyframes pageout {
  from {
      opacity: 1;
      visibility: visible;
      /* transform: rotate(-10deg);      */
  } 
  to {
      transform: translateY(100%);
  }
}
@keyframes fadein {
  from {
      opacity: 0;
      visibility: hidden;
  }
  to {
      opacity: 1;
      visibility: visible;
  }
}

#App {
  position: absolute;
  /* display: none; */
  left: 0;
  top: 0;
  box-sizing: border-box;
  padding: 0 5%;
  padding-top: 3%;
  height: 100vh;
  width: 100vw;
  /* z-index: 1; */
  background: url(./assets/background.jpg) no-repeat center center;
  background-size: 100% 100%;
  font-family: font1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
.menu-icon:hover {
  font-size: 115%;
  transition: 0.3s;
  cursor: pointer;
} 
.navbar {
  position: relative;
  display: flex;
  justify-content: space-between;
  overflow: hidden;
  height: 8%;
  font-size: 2.5rem;
  z-index: 3;
  color: rgb(160, 133, 133);
}
.navbar > span {
  width: 60%;
}
.project-name {
  cursor: pointer;
  animation: 'fadein' 3s;
  font-weight: bold;
}
.project-name:hover {
  opacity: 0.7;
}
.page-name {
  position: absolute;
  margin-left: 16%;
  font-size: 33%;
  font-weight: bold;
  height: 100%;
  top: 0;
  animation: 'fadein' 3s;
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
  color: rgb(160, 133, 133);
  z-index: 3;
  animation: 'fadein' 3s;
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
.account span:hover {
  /* font-size: 120%; */
  font-weight: bold;
  transition: 0.5s;
}
.app-menu {
  position: relative;
  z-index: 0;
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
  cursor: pointer;
}
.menu-list > div {
  margin-bottom: 2%;
}
.menu-list div:hover {
  font-size: 120%;
  transition: 0.5s;
}
.menu-icon {
  animation: 'fadein' 3s;
}
</style>
