<template>
  <div id="Carousel">
    <!-- <i @click="rotateL" class="btn-left fas fa-chevron-circle-left"></i> -->
    <div class="carousel">
      <img v-for="(recData,idx) in recDatas" :key="idx" @click="toRecDetail(recData.book_isbn)"
      :src="`http://j4a205.p.ssafy.io:8050/images/${recData.book_isbn}.jpg`" alt="" class="panel">
    </div>
    <!-- <i @click="rotateR" class="btn-right fas fa-chevron-circle-right"></i> -->
  </div>
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'Carousel',
  data: function () {
    return {
      recDatas: {},
      user_id: 0,
    }
  },
  methods: {
    rotateR: function () {
      const carousel = document.querySelector('.carousel')
      carousel.style.transform="rotateY(36deg)"
    },
    rotateL: function () {
      const carousel = document.querySelector('.carousel')
      carousel.style.transform="rotateY(-36deg)"
    },
    toRecDetail: function (isbn) {
      this.$router.push({name: 'Detail', params:{bookIsbn:isbn}})
    }
  },
  created: function () {

    if (localStorage.getItem('user_id')===null) {
      this.user_id = 0
    } else {
      this.user_id = localStorage.getItem('user_id')
    }
    axios.get(`${SERVER_URL}/recommends/${this.user_id}/list`)
      .then(res => {
        this.recDatas = res.data
        if (this.user_id===0) {
          this.recDatas = this.recDatas.splice(0,9)
        }
      })  
  }
}
</script>

<style>
@keyframes three-dimensions-circle {
  0% {
    transform: rotateY(0deg) rotate(0);
  }
  100% {
    transform: rotateY(-360deg) rotate(0);
  }
}
#Carousel {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  /* padding-left: 60%; */
  perspective: 700px;
  font-size: 150%;
}

.carousel {
  /* position: absolute; */
  width: 200px;
  height: 200px;
  transform-style: preserve-3d;
  transform: rotateY(-12deg);
  animation: three-dimensions-circle 28s linear infinite;
}
.panel {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  left: 0;
  top: 0;
  width: 130px;
  height: 170px;
  background: rgba(255,255,255,0.5);
  opacity: 0.8;
}
.panel:hover {
  width: 140px;
  height: 180px;
  transition: 0.5s;
}
.btn-left {
  position: absolute;
  left: 43%;
}
.btn-right {
  position: absolute;
  right: 4.5%;
}
.panel:nth-child(1) { 
  transform: rotateY(0deg)
          translateZ(290px);
}
.panel:nth-child(2) { 
  transform: rotateY(36deg) 
          translateZ(290px); 
}
.panel:nth-child(3) { 
  transform: rotateY(72deg) 
          translateZ(290px);
}
.panel:nth-child(4) { 
  transform: rotateY(108deg)
          translateZ(290px);
}
.panel:nth-child(5) { 
  transform: rotateY(144deg)
          translateZ(290px);
}
.panel:nth-child(6) { 
  transform: rotateY(180deg)
          translateZ(290px);  
}
.panel:nth-child(7) { 
  transform: rotateY(216deg)
          translateZ(290px);  
}
.panel:nth-child(8) { 
  transform: rotateY(252deg)
          translateZ(290px);  
}
.panel:nth-child(9) { 
  transform: rotateY(288deg)
          translateZ(290px);  
}
.panel:nth-child(10) { 
  transform: rotateY(324deg)
          translateZ(290px);  
}
</style>