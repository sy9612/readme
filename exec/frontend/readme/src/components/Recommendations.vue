<template>
  <div id="Recommendations">
    <div>
      <div v-if="this.jwt == null">
        <h2>금주의 베스트셀러</h2>
        <h4>회원가입을 통해 나만을 위한 도서 추천을 받아보세요!</h4>
      </div>
      <div v-else>
        <h2>{{ this.user_name }} 님을 위한 추천 도서</h2>
      </div>
      <recommend-list></recommend-list>
    </div>
    
    <div v-if="this.jwt == null"></div>
    <div v-else>
      <h2>{{ this.user_name }} 님과 동일 성별, 연령대의 인기 도서</h2>
      <age-list></age-list>
    </div>
    <div v-if="this.jwt == null"></div>
    <div v-else>
      <h2>{{ this.user_name }} 님의 MBTI 기반 추천 도서</h2>
      <mbti-list></mbti-list>
    </div>
  </div>
</template>

<
<script>
import RecommendList from './RecommendList.vue';
import MbtiList from './MbtiList.vue';
import AgeList from './AgeList.vue';

export default {
  name: 'Recommendations',
  components: { RecommendList, MbtiList, AgeList },
  created() {
    this.fnGetUsr();
  },
  props: {
    menuIsOpen: Boolean,
  },
  methods: {
    fnGetUsr: function () {
      const jwt = localStorage.getItem('jwt');
      const user_id = localStorage.getItem('user_id');
      const user_name = localStorage.getItem('username');
      this.user_id = user_id;
      this.user_name = user_name;
      this.jwt = jwt;
      // console.log(jwt);
    },
  },
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Recommendations')
      if (this.menuIsOpen === false) {
          page.style.display = 'block'
      } else {
        page.style.display = 'none'
        // page.style.transitionDuration = '10s'
        page.style.transitionTimingFunction = 'ease-out'
      }
    },
  },
  data: function () {
    return {
      user_id: '',
      user_name: '',
      jwt: '',
    };
  },
  created: function () {
    this.$emit('page','Recommendations')
    this.$emit('isHome', this.$route.name)
    this.fnGetUsr()
  }
};
</script>

<style>
#Recommendations {
  background: url(../assets/background.jpg) no-repeat center center;
  background-size: 100% 100%;
  position: absolute;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 19%;
  padding-top: 10%;
  overflow: scroll;
}
#Recommendations::-webkit-scrollbar {
  display: none;
}
</style>
