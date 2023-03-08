import { createRouter, createWebHistory } from 'vue-router'
import home from '../views/home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/game1',
    name: 'game1',
    component: () => import(/* webpackChunkName: "about" */ '../views/game1.vue')
  },
  {
    path: '/game2',
    name: 'game2',
    component: () => import(/* webpackChunkName: "about" */ '../views/game2.vue')
  },
  {
    path: '/game3',
    name: 'game3',
    component: () => import(/* webpackChunkName: "about" */ '../views/game3.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
