<template>
  <div id="RecMain">
    <Carousel />
  </div>
</template>

<script>
import Carousel from '@/components/Carousel'

export default {
  name: 'RecMain',
  components: {
    Carousel
  },
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
  background: url(../assets/recommendation.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  height: 100vh;
  width: 100vw;
  color: white;
  font-weight: bold;
  z-index: 1;
}
</style>