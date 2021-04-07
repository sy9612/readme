<<<<<<< HEAD

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

=======
<template>
  <div id="Recommendations">
    <div>
      <h>나만의 추천 도서</h>
      <recommend-list></recommend-list>
    </div>
    <div>
      <h>성별, 연령대별 추천 도서</h>
      <age-list></age-list>
    </div>
    <div>
      <h>MBTI별 추천 도서</h>
      <mbti-list></mbti-list>
    </div>
  </div>
</template>

<
<script>
export default {
  name: 'Recommendations',
  data: function () {
    return {};
  },
};
>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
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
<<<<<<< HEAD
  padding: 0 20%;
  padding-top: 10%;
}

=======
  padding: 0 10%;
  padding-top: 10%;
}
>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
</style>
