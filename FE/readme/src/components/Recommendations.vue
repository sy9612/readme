
<template>

  <div id = "Recommendations">
    <a @click="wishMethod" :style="wishstyle" style="cursor:pointer; margin-right: 15px; font-size: 30px">찜한 도서</a>
    <a @click="readMethod" :style="readstyle" style="cursor:pointer; font-size: 30px">읽은 도서</a>

    <div v-if="wish"><wish-list></wish-list></div>
    <div v-if="read"><read-list></read-list></div>
  </div>

  
</template>

<script>
import WishList from './WishList.vue'
import ReadList from './ReadList.vue'

export default {
  name: 'Recommendations',
  components: { WishList, ReadList },
  data: function(){
    return{
      wishstyle:{
        textDecoration: 'underline',
      },
      readstyle:{
        textDecoration: '',
      },
      wish: true,
      read: false,
    };
  },
  
  methods: {
  	wishMethod:function() {
      this.wish = true
      this.read = false
      this.readstyle.textDecoration = ''
      this.wishstyle.textDecoration = 'underline'


    },
    readMethod: function(){
      this.wish = false
      this.read = true
      this.readstyle.textDecoration = 'underline'
      this.wishstyle.textDecoration = ''
    },
  }
  
}

</script>

<style>
#Recommendations {
  position: absolute;
  background: #d7b9a1;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 20%;
  padding-top: 10%;
}

</style>
