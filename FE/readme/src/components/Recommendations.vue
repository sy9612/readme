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
  padding: 0 10%;
  padding-top: 10%;
}
</style>
