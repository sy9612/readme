import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import MyPage from "../components/MyPage.vue";
import Search from "../components/Search.vue";

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
  },
];

const router = new VueRouter({
  routes,
});

export default router;
