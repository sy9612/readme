import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import MyPage from "../components/MyPage.vue";
import Search from "../components/Search.vue";
<<<<<<< HEAD

Vue.use(BootstrapVue);
=======
import Report from "../components/Report.vue";
import Detail from "../components/Detail.vue";
import Recommendations from '../components/Recommendations.vue';
import BootstrapVue from 'bootstrap-vue';
import VueCarousel from 'vue-carousel';

Vue.use(VueCarousel);
Vue.use(BootstrapVue);

>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/MyPage',
    name: 'MyPage',
    component: MyPage
  },
  {
    path: '/Search',
    name: 'Search',
    component: Search
  },
  {
<<<<<<< HEAD
    path: '/Recommendations',
    name: 'Recommendations',
    component: Recommendations
  },
  {
    path: '/WishList',
    name: 'WishList',
    component: WishList
  },
  {
    path: '/ReadList',
    name: 'ReadList',
    component: ReadList
=======
    path: '/Report/:bookId',
    name: 'Report',
    component: Report
  },
  {
    path: '/Detail/:bookId',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/Recommendations',
    name: 'Recommendations',
    component: Recommendations
>>>>>>> a913177d954384e359e7f4c53544b6789d8462c0
  },
];

const router = new VueRouter({
  routes,
});

export default router;
