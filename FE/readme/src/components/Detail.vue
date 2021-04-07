<template>
  <div id="Detail">
    <div class="detail_wrapper">

      <div class="detail_content">
        <div class="book_info">
          <img src="../assets/harry.jpg" alt="">
          <div class="book_contents">
            <p>해리포터와 마법사의 돌</p>
            <p>장르: 공포</p>
            <p>상세내용: Lorem ipsum dolor sit amet consectetur, adipisicing elit. Qui, doloribus.</p>
          </div>
        </div>
        <div class="review_form">
          <p>리뷰 작성</p>
          <div class="rating">
            <p>평점</p>
            <StarRating @selectStar="selectStar" />
          </div> 
          <textarea v-model="reviewContent" cols="30" rows="10"></textarea>
        </div>
      </div>

      <div class="right_detail">
        <div v-if="reviewIsOpen===false" class="reviews">
          <div>Reviews</div>
          <div class="review_container">
            <div @click="openReview(idx)" v-for="(review,idx) in right_detail" :key="idx" class="review">
              <div>{{ review.content }}</div>
              <div><i class="fas fa-star"></i>X{{ review.rate }}</div>
              <div>{{ review.writer }}</div>
            </div>
          </div>
        </div>

        <div v-if="reviewIsOpen===true" class="review_detail">
          <p @click="closeReview">{{ selectedReview.writer }}님의 리뷰</p>
          <div>
            <p>평점  <i class="review_rate fas fa-star"></i>X{{ selectedReview.rate }}</p>
          </div>
          <p>{{ selectedReview.content }}</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import StarRating from '@/components/StarRating'

export default {
  name: 'Detail',
  components: {
    StarRating
  },
  data: function () {
    return {
      right_detail: [
        {
        content: '별로야아니아니아ㅣㄴ아니아니아니라',
        rate: 3,
        writer: '싸피', 
      },
        {
        content: '별로야아니아니아ㅣㄴ아니아니아니라',
        rate: 3,
        writer: '싸피', 
      },
        {
        content: '별로야아니아니아ㅣㄴ아니아니아니라',
        rate: 3,
        writer: '싸피', 
      },
      ],
      reviewContent: '',
      rate: 0,
      reviewIsOpen: false,
      selectedReview: {},
    }
  },
  methods: {
    openReview: function (idx) {
      const review = this.right_detail[idx]
      this.selectedReview = review
      this.reviewIsOpen = true
      console.log(this.selectedReview)

    },
    closeReview: function () {
      this.reviewIsOpen = false
    },
    selectStar: function (ratedStar) {
      this.rate = ratedStar
    },
  },
}
</script>

<style>
#Detail {
  position: absolute;
  display: flex;
  flex-direction: column;
  background: #d7b9a1;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 22%;
  padding-top: 7%;
}
.detail_wrapper {
  position: relative;
  display: flex;
  justify-content: space-between;
  margin-top: 5%;
  height: 100%;
  width: 100%;
  background: rgb(166, 180, 177);
  border-radius: 20px;
  padding: 2%;
}
.detail_wrapper > div {
  position: relative;
  width: 49.8%;
  background: rgb(191, 201, 200);
  border-radius: 20px;
  padding: 1%;
  box-shadow: 5px 5px;
}
.book_info {
  position: relative;
  display: flex;
  justify-content: space-between;
  height: 50%;
  overflow: hidden;
}
.book_info img {
  height: 100%;
  width: 48%;
  /* border-radius: 10px; */
}
.book_contents {
  width: 48%;
}
.review_form {
  position: absolute;
  margin-top: 2%;
  height: 48%;
  width: 95%;
  background: white;
  border-radius: 10px;
  padding: 0.5% 3%;
  box-sizing: border-box;
}
.review_form p {
  text-align: center;
  margin-bottom: 3%;
}
.review_form textarea {
  width: 98%;
  font-family: font1;
}
.rating {
  display: flex;
  margin-bottom: 3%;
}
.rating p {
  margin-bottom: 0;
  margin-top: 1%;
  margin-right: 3%;
}
.right_detail > div > div:nth-child(1) {
  text-align: center;
  font-size: 150%;
  margin-bottom: 3%;
}
.right_detail > div {
  position: relative;
  width: 100%;
  height: 100%;
}
.right_detail textarea {
  position: relative;
  font-family: font1;
  /* margin-top: 10%; */
  width: 100%;
  height: 90%;
  background: none;
  border: none;
  outline: none;
  margin-bottom: 2%;
}
.review_container {
  height: 97%;
}
.review {
  display: flex;
  box-sizing: border-box;
  height: 8.5%;
  padding: 2.5% 0;
  /* padding-bottom: 2%; */
  border: ivory solid 2px;
  cursor: pointer;
}
.review:hover {
  opacity: 0.5;
}
.review div:nth-child(1) {
  position: relative;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  width: 60%;
  height: 100%;
  overflow: hidden;
  white-space: normal;
  text-overflow: ellipsis;
}
.review div {
  margin: 0 2%;
}
.review_detail p {
  text-align: center;
  font-size: 150%;
  
}
.review_detail > p:nth-child(1) {
  cursor: pointer;
}
.review_detail > p:nth-child(1):hover {
  opacity: 0.5;
}
.review_detail div:nth-child(1) {
  display: flex;
}
.review_rate {
  margin: 0 1%;
}
</style>