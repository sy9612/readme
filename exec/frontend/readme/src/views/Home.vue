<template>
  <div id="Home">
    <!-- <i class="homemenu fas fa-bars"></i> -->
    <div id="homepage">
      <div class="home-message">
        <div>도서 추천 서비스 - README</div>
        <div>여러분의 독서고민</div>
        <div>우리가 해결해드려요</div>
      </div>
    </div>
    <div class="scroll">
      <div @click="toUp" v-if="pageNo!==0"><i class="fas fa-2x fa-chevron-circle-up"></i></div>
      <div @click="toDown" v-if="pageNo!==1"><i class="fas fa-2x fa-chevron-circle-down"></i></div>
    </div>
    <RecMain />
  </div>

</template>

<script>
import RecMain from '@/components/RecMain'

export default {
  name: 'Home',
  data: function () {
    return {
      pageNo: 0,
      pagename: 'Home',
    }
  },
  components: {
    RecMain,
  },
  props: {
    menuIsOpen: Boolean,
  },
  methods: {
    toUp: function () {
      this.pageNo -= 1
      const page = document.getElementById('homepage')
      page.style.transform = 'translateY(0)'
      page.style.transition = '1s'
      this.$emit('page','Home')
    },
    toDown: function () {
      this.pageNo += 1
      const page = document.getElementById('homepage')
      page.style.transform = 'translateY(-100%)'
      page.style.transition = '1s'
      this.$emit('page','Recommendation for you')
  
    },
  },
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Home')
      if (this.menuIsOpen === false) {
          page.style.transform = 'scale(1)'
      } else {
        page.style.transform = 'scale(0)'
        page.style.transitionDuration = '0.4s'
        page.style.transitionTimingFunction = 'ease-out'
      }
    },
  },
  created: function () {
    this.$emit('page','Home')
    this.$emit('isHome', this.$route.name)
  }
}
</script>

<style>
#Home {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
#homepage {
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  align-items: center;
  flex-direction: column;
  /* width: 100%;
  height: 100%; */
  background: url(../assets/Home.jpg) no-repeat center center;
  background-size: 100% 100%;
  height: 100%;
  width: 100%;
  color: white;
  font-weight: bold;
  z-index: 2;
}
.homemenu {
  position: absolute;
  right: 3%;
  top: 8%;
  height: 10%;
  width: 10%;
  z-index: 3;
}
.scroll {
  position: absolute;
  display: flex;
  /* justify-content: center; */
  top: 90%;
  left: 50%;
  z-index: 3;
}
.scroll:hover {
  font-size: 120%;
  transition: 0.3s;
  opacity: 0.8;
  color: #fff;
}
.home-message {
  position: absolute;
  top: 34%;
  height: 40%;
  width: 30%;
  font-size: 150%;
  animation: 'fadein' 3s;
  transform: translate(-80px);
}
.home-message div {
  margin-bottom: 3%;
}
.home-message div:nth-child(1) {
  font-size: 50%;
}
.home-message div:nth-child(n+2) {
  font-size: 200%;
}
.home-message div:nth-child(3) {
  color: #2c3e50;
}
</style>
