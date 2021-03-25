<template>
  <div id="main">

    <div class="scroll">
      <div>up</div>
      <div @click="nextMainPage">down</div>
    </div>
    <div class="main-message" v-if="signupIsOpen===false && loginIsOpen===false">
      <div>도서 추천 서비스-README</div>
      <div>여러분의 독서고민</div>
      <div>우리가 해결해드려요</div>
    </div>
    <Signup v-if="signupIsOpen===true && loginIsOpen===false" :signupIsOpen='signupIsOpen' />
    <Login v-if="loginIsOpen===true && signupIsOpen===false" />
  </div>
  
</template>

<script>
import Signup from '@/components/Signup'
import Login from '@/components/Login'


export default {
  name: 'Main',
  data: function () {
    return {

    }
  },
  components: {
    Signup,
    Login,
  },
  props: {
    mainIsOpen: Boolean,
    signupIsOpen: Boolean,
    loginIsOpen: Boolean,
  },
  methods: {
    nextMainPage: function () {
      console.log(2)
      this.$router.push({name:'DataStatus'})
    }
  },
  watch: {
    mainIsOpen: function () {
      const page = document.getElementById('main')
      if (this.mainIsOpen === true) {
          page.style.display = 'flex'
      } else {
        page.style.display = 'none'
        page.style.transitionDuration = '10s'
        page.style.transitionTimingFunction = 'ease-out'
      }
    },
    signupIsOpen: function () {

    },

  }
}
</script>

<style>
#main {
  position: relative;
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
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