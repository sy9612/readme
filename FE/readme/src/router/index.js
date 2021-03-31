import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import MyPage from "../components/MyPage.vue";
import DataStatus from '../components/DataStatus.vue';

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
    path: '/DataStatus',
    name: 'DataStatus',
    component: DataStatus
  },
];

const router = new VueRouter({
  routes,
});

export default router;
