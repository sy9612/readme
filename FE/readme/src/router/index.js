import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import MyPage from "../components/MyPage.vue";
import Search from "../components/Search.vue";
import Report from "../components/Report.vue";
import Detail from "../components/Detail.vue";
import Recommendations from '../components/Recommendations.vue';
import BootstrapVue from 'bootstrap-vue';
import VueCarousel from 'vue-carousel';


const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(() => {
        return window.location.reload()
    })
};

Vue.use(VueCarousel);
Vue.use(BootstrapVue);

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
    path: '/Report/:bookIsbn',
    name: 'Report',
    component: Report
  },
  {
    path: '/Detail/:bookIsbn',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/Recommendations',
    name: 'Recommendations',
    component: Recommendations
  },
];

const router = new VueRouter({
  routes,
});

export default router;
