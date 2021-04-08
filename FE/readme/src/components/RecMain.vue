<template>
  <div id="RecMain">
    <Carousel />
  </div>
</template>

<script>
import Carousel from '@/components/Carousel'
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'RecMain',
  components: {
    Carousel
  },
  // created: function () {
  //   const user_id = localStorage.getItem('user_id')
  //   axios.get(`${SERVER_URL}/recommends/${user_id}/list`)
  //     .then(res => {
  //       console.log(res)
  //       // this.bookinfo = res.data.book
  //       // this.maincategory = res.data.maincategory
  //       // this.subcategory = res.data.subcategory
  //       // this.imgsrc = `http://j4a205.p.ssafy.io:8050/images/${this.bookinfo.book_isbn}.jpg`
  //     })  
    
  // }
}
</script>

<style>
@keyframes pageshowing {
  from {
    transform: translateY(100%);
  }
  to {
    /* transform: translateY(0); */
  }
}

#RecMain {
  /* animation: 'pageshowing' 2s; */
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  align-items: center;
  flex-direction: column;
  /* width: 100%;
  height: 100%; */
  background: url(../assets/backrec.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  height: 100vh;
  width: 100vw;
  color: white;
  font-weight: bold;
  z-index: 1;
}
</style>