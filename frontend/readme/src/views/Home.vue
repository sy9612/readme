<template>
  <div id="home">
    <div class="main-title">
      README
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
.main-title {
  position: absolute;
  left: 10%;
  top: 10%;
  height: 5%;
  width: 10%;
  font-size: 2.5rem;
  z-index: 1;
}
</style>
