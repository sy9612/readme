<template>
  <div id="Data-status">

  </div>
</template>

<script>
export default {
  name: 'datastatus',

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

#Data-status {
  animation: 'pageshowing' 2s;
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  align-items: center;
  flex-direction: column;
  /* width: 100%;
  height: 100%; */
  background: url(../assets/DataStatus.jpg) no-repeat center center;
  background-size: 100vw 100vh;
  height: 100vh;
  width: 100vw;
  color: white;
  font-weight: bold;
}
</style>