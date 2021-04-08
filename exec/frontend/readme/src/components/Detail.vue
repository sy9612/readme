<template>
  <div id="Detail">
    <div class="detail_wrapper">

      <div class="detail_content">
        <div class="book_info">
          <img :src="imgsrc"/>
          <div class="book_contents">
            <p @click="toReport"> {{ bookinfo.book_title }}</p>
            <p>{{ bookinfo.book_author }}</p>
            <p>{{ maincategory }}</p>
            <p>{{ subcategory }}</p>
          </div>
        </div>
        <p>{{ bookinfo.book_description }}</p>
        <!-- <div class="review_form">
          <p>리뷰 작성</p>
          <div class="rating">
            <p>평점</p>
            <StarRating @selectStar="selectStar" />
            <button @click="postReview">작성</button>
          </div> 
          <textarea v-model="params.review_content" cols="30" rows="10"></textarea>
        </div> -->
      </div>

      <div class="right_detail">
        <div v-if="reviewIsOpen===1" class="reviews">
          <div><span @click="openForm">Reviews</span></div>
          <div class="review_container">
            <div @click="openReview(idx)" v-for="(review,idx) in reviews" :key="idx" class="review">
              <div>{{ review.review_content }}</div>
              <div><i class="fas fa-star" style="color:#fd4"></i>X{{ review.review_rating }}</div>
              <div>{{ review.user_id }}</div>
            </div>
          </div>
        </div>

        <div v-if="reviewIsOpen===2" class="review_detail">
          <p @click="closeReview">{{ selectedReview.user_id }}님의 리뷰</p>
          <div>
            <p style="font-size:130%; margin:8% 0">평점  <i class="review_rate fas fa-star"></i>X{{ selectedReview.review_rating }}</p>
          </div>
          <p>{{ selectedReview.review_content }}</p>
        </div>

        <div v-if="reviewIsOpen===3" class="review_form">
          <p @click="closeReview">리뷰 작성하기</p>
          <StarRating @selectStar="selectStar" />
          <textarea v-model="params.review_content" cols="20" rows="10"></textarea>
          <b-button @click="postReview" pill variant="outline-secondary">작성완료</b-button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import StarRating from '@/components/StarRating'
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'Detail',
  components: {
    StarRating
  },
  props: {
    menuIsOpen: Boolean,
  },
  data: function () {
    return {
      reviews: {},
      params: {
        user_id: '',
        review_rating: 0,
        review_content: '',
      },
      reviewIsOpen: 1,
      selectedReview: {},
      bookinfo: {},
      maincategory: '',
      subcategory: '',
      imgsrc: '',
    }
  },
  methods: {
    openReview: function (idx) {
      const review = this.reviews[idx]
      this.selectedReview = review
      this.reviewIsOpen = 2

    },
    closeReview: function () {
      this.reviewIsOpen = 1
    },
    selectStar: function (ratedStar) {
      this.params.review_rating = ratedStar
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    postReview: function () {
      const isbn = this.$route.params.bookIsbn
      axios.post(`${SERVER_URL}/books/review/${isbn}`, this.params)
        .then(res => {
          this.reviewIsOpen = 1
          this.params.review_content = ''
          alert('작성되었습니다!')
        })  
    },
    openForm: function () {
      this.reviewIsOpen = 3
    },
    toReport: function () {
      if (localStorage.getItem('jwt')) {
        const isbn = this.$route.params.bookIsbn
        this.$router.push({name: 'Report', params:{bookIsbn:isbn}})    
      }

    },

  },
  watch: {
    menuIsOpen: function () {
      const page = document.getElementById('Detail')
      if (this.menuIsOpen === false) {
          page.style.transform = 'scale(1)'
      } else {
        page.style.transform = 'scale(0)'
        page.style.transitionDuration = '0.4s'
        page.style.transitionTimingFunction = 'ease-out'
      }
    },
  },
  created: function () {
    this.$emit('isHome', this.$route.name)
    this.$emit('page','BookDetail')
  //   const config = this.setToken()
    const isbn = this.$route.params.bookIsbn
    this.params.user_id = localStorage.getItem('user_id')
  //   console.log(user_id)
    axios.get(`${SERVER_URL}/books/${isbn}`)
      .then(res => {
        this.bookinfo = res.data.book
        this.maincategory = res.data.maincategory
        this.subcategory = res.data.subcategory
        this.imgsrc = `http://j4a205.p.ssafy.io:8050/images/${this.bookinfo.book_isbn}.jpg`
      }) 
    axios.get(`${SERVER_URL}/books/review/${isbn}`)   
      .then(res => {
        this.reviews = res.data
      }) 
  }
}
</script>

<style>
#Detail {
  position: absolute;
  display: flex;
  flex-direction: column;
  background: url(../assets/background.jpg) no-repeat center center;
  background-size: 100% 100%;
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
  box-sizing: border-box;
  justify-content: space-between;
  margin-top: 5%;
  height: 93%;
  width: 100%;
  background: rgba(165, 142, 142, 0.5);
  border-radius: 20px;
  padding: 2%;
  opacity: 0.8;
}
.detail_wrapper > div {
  position: relative;
  width: 49.8%;
  background: rgb(250, 248, 247);
  border-radius: 20px;
  padding: 1%;
  box-shadow: 5px 5px;
}
.detail_content {
  position: relative;
  height: 100%;
}
.detail_content > p {
  position: relative;
  box-sizing: border-box;
  margin-top: 2%;
  padding: 2% 3%;
  height: 44%;
  overflow: auto;
}
.detail_content > p::-webkit-scrollbar {
  display: none;
}
.book_info {
  position: relative;
  display: flex;
  justify-content: space-between;
  height: 50%;
  overflow: hidden;
  padding: 1% 3%;
  /* box-sizing: border-box; */
}
.book_info img {
  height: 100%;
  width: 48%;
  /* border-radius: 10px; */
}
.book_contents {
  /* box-sizing: border-box; */
  position: relative;
  width: 48%;
  height: 10%;
}
.book_contents p {
  overflow: auto;
}
.book_contents p:nth-child(1) {
  font-weight: bold;
  font-size: 115%;
  margin-top: 5%;
  cursor: pointer;
}
.book_contents p:nth-child(1):hover {
  opacity: 0.7;
}
.book_contents p:nth-child(2) {
  /* font-weight */
  font-size: 110%;
}
.review_form {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 2%;
  height: 48%;
  width: 95%;
  /* background: white; */
  border-radius: 10px;
  padding: 0.5% 3%;
  box-sizing: border-box;
}
.review_form p {
  text-align: center;
  margin-bottom: 7%;
  font-size: 150%;
  font-weight: bold;
  cursor: pointer;
}
.review_form p:hover {
  opacity: 0.5;
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
.right_detail {
  position: relative;
  height: 100%;
  overflow: hidden;
}
.right_detail > div > div:nth-child(1) {
  text-align: center;
  font-size: 150%;
  margin: 5% 0;
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
  height: 62%;
  background: wheat;
  border: none;
  outline: none;
  margin-top: 8%;
  margin-bottom: 5%;
  border-radius: 10px;
  font-size: 108%;
}
.reviews {
  position: relative;
  height: 80%;
}
.reviews span {
  cursor: pointer;
  font-weight: bold;
}
.reviews span:hover {
  opacity: 0.5;
}
.review_container {
  height: 85%;
  overflow: auto;
}
.review_container::-webkit-scrollbar {
  display: none;
}
.review {
  display: flex;
  box-sizing: border-box;
  height: 10%;
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
}
.review_detail > p:nth-child(1) {
  cursor: pointer;
    font-size: 150%;
  font-weight: bold;
}
.review_detail p:nth-child(2) {
    font-size: 150%;
  /* font-weight: bold; */
}
.review_detail > p:nth-child(1):hover {
  opacity: 0.5;
}
.review_detail div:nth-child(1) {
  display: flex;
}
.review_rate {
  margin: 0 1%;
  color: #fd4;
}
</style>