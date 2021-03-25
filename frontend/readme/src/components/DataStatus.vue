<template>
  <div id="data-status">
    <div @click="upPage">up</div>
  </div>
</template>

<script>
export default {
  name: 'dataStatus',
  methods: {
    upPage: function () {
      this.$router.push({name:'Home'})
    }
  }
}
</script>

<style>
#data-status {
  position: relative;
  display: flex;
  align-items: center;
  flex-direction: column;
  background: url(../assets/DataStatus.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  height: 100vh;
  width: 100vw;
}
</style>