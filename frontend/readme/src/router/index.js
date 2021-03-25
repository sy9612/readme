import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import DataStatus from '../components/DataStatus.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/datastatus',
    name: 'DataStatus',
    component: DataStatus,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
