<template>
  <div id="MyPage">
    <div class="mypage-list">
      <span>찜 목록</span>
      <span>읽는 중</span>
      <span>다 읽은 책</span>
      <span>책 쌓기</span>

      <button @click="clickDib">누르면 책 찜</button>
      <div v-if="clickedDib">찜했다!</div>
      <div v-else>찜 안했다!</div>
      <button @click="clickMyList">내찜리스트</button>
    </div>
      <div>
        <button @click="sendReview">리뷰 보내보자!</button>
      </div>
      
      <div>
        <button @click="updateReview">리뷰 수정</button>
      </div>
        <div>
        <button @click="deleteReview">리뷰 삭제</button>
      </div>
      <div>
        <button @click="bookDetail">700번책 세부내용</button>
      </div>

      <div>
        <button @click="mainCategory">메인 카테고리들</button>
      </div>
      <div>
        <button @click="subCategory">9번 메인의 서브 카테고리들</button>
      </div>
  </div>
</template>

<script>
const SERVER_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: 'MyPage',
  data: function () {
    return {
      clickedDib:false,
      //임의로 넣어둔 값임!
      user_id:1,
      book_id:700,
      review_rating:3,
      review_content:"아진짜 너무 재밌어요!!",
    }
  },
  created: function () {
    const config = this.setToken()
    //book 리스트를 전부 다 가져오는 url
    axios.get(`${SERVER_URL}/books/list`,config)
      .then(res => {
        console.log(res)
      })
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
  //내 찜 리스트...
    clickMyList: function(){
        const credentials = {
          user_id:this.user_id,
        }
      axios.post(`${SERVER_URL}/accounts/dibsList`,credentials)
      .then(({data}) => {
        console.log(data)
      })
      .catch( (err) => {
        console.log(err)
      })
    },

    //찜 클릭 or 해제 -> clickedDib이 true냐 false냐에 따라 버튼 색? 등을 다르게 하면 될듯
    clickDib: function(){
        const credentials = {
          user_id:this.user_id,
        }
      //accounts/clickDibs/{book_id}
      axios.post(`${SERVER_URL}/accounts/clickDibs/702`,credentials)
      .then(({data}) => {
        this.clickedDib=data.dibSelect
      })
      .catch( (err) => {
        console.log(err)
      })
    },
    //bookDetail에서 myreview가 비어있을 때 리뷰작성폼이 보이게 하면 중복 방지 가능 
    sendReview: function(){
      const credentials = {
          user_id:this.user_id,
          book_id:this.book_id,
          review_rating:this.review_rating,
          review_content:this.review_content,
        }
        
        axios.post(`${SERVER_URL}/books/createReview`,credentials)
        .then(({data}) => {
          console.log(data)
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    //bookDetail에서 myreview에 내용이 들어가 있으면 우선 그 리뷰를 보여주고 수정 버튼을 클릭 시 ... 수정 가능하게 ?  
    updateReview: function(){
      const credentials = {
          user_id:this.user_id,
          book_id:this.book_id,
          review_rating:4,
          review_content:"바꾼 내용!",
        }
        //books/updateReview/{review_id}
        axios.post(`${SERVER_URL}/books/updateReview/7`,credentials)
        .then(({data}) => {
          console.log(data)
        })
        .catch( (err) => {
          console.log(err)
        })
    },

    deleteReview: function(){
        //books/deleteReview/{review_id}
      axios.delete(`${SERVER_URL}/books/deleteReview/7`)
        .then(({data}) => {
          console.log(data)
        })
        .catch( (err) => {
          console.log(err)
        })
    },
    mainCategory:function(){
      //메인 카테고리 목록 가져오기 (main_category 테이블 내용)
      axios.post(`${SERVER_URL}/books/maincategory`)
      .then(({data}) => {
        console.log(data)
      })
      .catch( (err) => {
        console.log(err)
      })
    },

    //main카테고리의 sub카테고리들 가져오기
    subCategory:function(){
      //books/subcategory/{main_id}
      axios.post(`${SERVER_URL}/books/subcategory/9`)
      .then(({data}) => {
        console.log(data)
      })
      .catch( (err) => {
        console.log(err)
      })
    },

    //카테고리 별 도서 목록 가져오기
    categorybooks:function(){
      const credentials = {
          main_id:9, //main_id가 0이면 '전체' 
          sub_id:1 //아마 select box로 선택하게끔 하겠지? sub_id가 1이면 '전체'
        }
        
        axios.post(`${SERVER_URL}/books/categorybooks`,credentials)
        .then(({data}) => {
          console.log(data)
        })
        .catch( (err) => {
          console.log(err)
        })
    },

    //책 상세정보 + 내가 찜했는지 여부 + 리뷰 달았는지 + 책 카테고리
    bookDetail: function(){
      const credentials = {
        user_id:this.user_id,
      }
      //books/{book_id}
      axios.post(`${SERVER_URL}/books/700`,credentials)
      .then(({data}) => {
        console.log(data)
      })
      .catch( (err) => {
        console.log(err)
      })
    },
  }
}   
</script>

<style>
#MyPage {
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
.mypage-list {
  /* border: 2px solid red; */
}
.mypage-list span {
  margin-right: 5%;
}
.mypage-list span:nth-child(1) {
  font-weight: bold;
  font-size: 115%;
}
</style>