<template>
  <div>
    <carousel
      class="card-carousel-wrapper"
      :navigation-click="true"
      :per-page="4"
      :mouse-drag="false"
    >
      <div v-if="this.items == 0">
        읽은 도서가 없습니다. README를 통해 추천받은 책을 읽어보세요~
      </div>
        <slide v-else
          class="card-carousel"
          v-for="item in this.items"
          v-bind:key="item.book_title"
        >
          <div class="card-carousel--overflow-container">
            <div class="card-carousel-cards">
              <div class="card-carousel--card">
                <img :src="require(`../assets/${item.book_isbn}.jpg`)" />
                <div class="card-carousel--card--footer">
                  <p>{{ item.book_title }}</p>
                  <p class="tag">
                    {{ item.book_author }}
                  </p>
                  <p style="color: #f5d107">
                    ★ {{ fnRateList(item.rating_avg) }} ({{
                      fnRatecntList(item.rating_cnt)
                    }}명)
                  </p>
                </div>
              </div>
            </div>
          </div>
        </slide>
    </carousel>
  </div>
</template>

<script>
const SERVER_URL = 'http://127.0.0.1:8000';
import axios from 'axios';
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: 'RecommendList',
  components: { Carousel, Slide },
  data() {
    return {
      // path: "http://j4a205.p.ssafy.io:8050/",
      user_id: 2,
      currentOffset: 0,
      windowSize: 4,
      paginationFactor: 220,
      items: [],
    };
  },
  computed: {
    atEndOfList() {
      return (
        this.currentOffset <=
        this.paginationFactor * -1 * (this.items.length - this.windowSize)
      );
    },
    atHeadOfList() {
      return this.currentOffset === 0;
    },
  },
  created() {
    this.fnGetList();
  },

  methods: {
    fnRateList: function (rating_avg) {
      if (rating_avg.review_rating__avg == null) return 0;
      else return rating_avg.review_rating__avg;
    },
    fnRatecntList: function (rating_cnt) {
      if (rating_cnt == null) return 0;
      else return rating_cnt.review_rating__cnt;
    },

    moveCarousel(direction) {
      // Find a more elegant way to express the :style. consider using props to make it truly generic
      if (direction === 1 && !this.atEndOfList) {
        this.currentOffset -= this.paginationFactor;
      } else if (direction === -1 && !this.atHeadOfList) {
        this.currentOffset += this.paginationFactor;
      }
    },

    fnGetList() {
      axios
        .get(`${SERVER_URL}//recommends/` + this.user_id + `/list`)
        .then((res) => {
          this.items = res.data;
          console.log(res.data);
        });
    },
  },
};
</script>

<style>
#RecommendList {
  /* position: absolute; */
  background: #d7b9a1;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  /* padding: 0 20%; */
  padding-top: 10%;
}
body {
  background: #f8f8f8;
  color: #2c3e50;
  font-family: 'Source Sans Pro', sans-serif;
}

.card-carousel-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 40px;
  color: #666a73;
}
/* 
.card-carousel {
  display: flex;
  justify-content: center;
  width: 100%;
} */
.card-carousel--overflow-container {
  overflow: hidden;
}
.card-carousel--nav__left,
.card-carousel--nav__right {
  display: inline-block;
  width: 15px;
  height: 15px;
  padding: 10px;
  box-sizing: border-box;
  border-top: 2px solid black;
  border-right: 2px solid black;
  cursor: pointer;
  margin: 0 20px;
  transition: transform 150ms linear;
}
.card-carousel--nav__left[disabled],
.card-carousel--nav__right[disabled] {
  opacity: 0.2;
  border-color: black;
}
.card-carousel--nav__left {
  transform: rotate(-135deg);
}
.card-carousel--nav__left:active {
  transform: rotate(-135deg) scale(0.9);
}
.card-carousel--nav__right {
  transform: rotate(45deg);
}
.card-carousel--nav__right:active {
  transform: rotate(45deg) scale(0.9);
}

.card-carousel-cards {
  display: flex;
  transition: transform 150ms ease-out;
  transform: translatex(0px);
}
.card-carousel-cards .card-carousel--card {
  width: 200px;
  height: 330px;
  margin: 0 10px;
  cursor: pointer;
  box-shadow: 0 4px 15px 0 rgba(40, 44, 53, 0.06),
    0 2px 2px 0 rgba(40, 44, 53, 0.08);
  background-color: #fff;
  border-radius: 4px;
  z-index: 3;
  margin-bottom: 2px;
}
.card-carousel-cards .card-carousel--card:first-child {
  margin-left: 0;
}
.card-carousel-cards .card-carousel--card:last-child {
  margin-right: 0;
}
.card-carousel-cards .card-carousel--card img {
  vertical-align: bottom;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  transition: opacity 150ms linear;
  user-select: none;
  width: 200px;
  height: 200px;
}
.card-carousel-cards .card-carousel--card img:hover {
  opacity: 0.5;
}
.card-carousel-cards .card-carousel--card--footer {
  border-top: 0;
  padding: 7px 15px;
}
.card-carousel-cards .card-carousel--card--footer p {
  padding: 3px 0;
  margin: 0;
  margin-bottom: 2px;
  font-size: 19px;
  font-weight: 500;
  color: #2c3e50;
  user-select: none;
}
.card-carousel-cards .card-carousel--card--footer p.tag {
  font-size: 11px;
  font-weight: 300;
  padding: 4px;
  background: rgba(40, 44, 53, 0.06);
  display: inline-block;
  position: relative;
  margin-left: 4px;
  color: #666a73;
}
.card-carousel-cards .card-carousel--card--footer p.tag:before {
  content: '';
  float: left;
  position: absolute;
  top: 0;
  left: -12px;
  width: 0;
  height: 0;
  border-color: transparent rgba(40, 44, 53, 0.06) transparent transparent;
  border-style: solid;
  border-width: 8px 12px 12px 0;
}
.card-carousel-cards .card-carousel--card--footer p.tag.secondary {
  margin-left: 0;
  border-left: 1.45px dashed white;
}
.card-carousel-cards .card-carousel--card--footer p.tag.secondary:before {
  display: none !important;
}
.card-carousel-cards .card-carousel--card--footer p.tag:after {
  content: '';
  position: absolute;
  top: 8px;
  left: -3px;
  float: left;
  width: 4px;
  height: 4px;
  border-radius: 2px;
  background: white;
  box-shadow: 0px 0px 0px #004977;
}

h1 {
  font-size: 3.6em;
  font-weight: 100;
  text-align: center;
  margin-bottom: 0;
  color: black;
}
</style>
