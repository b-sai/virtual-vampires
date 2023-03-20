import { createRouter, createWebHistory } from 'vue-router'
import home from '../views/home.vue'
import {auth} from '../firebase'
import Login from '../views/login.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/game1',
    name: 'game1',
    component: () => import(/* webpackChunkName: "about" */ '../views/game1.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/game2',
    name: 'game2',
    component: () => import(/* webpackChunkName: "about" */ '../views/game2.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/game3',
    name: 'game3',
    component: () => import(/* webpackChunkName: "about" */ '../views/game3.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if(to.path === '/login' && auth.currentUser){
    next('/')
    return;
  }
  if(to.matched.some(record => record.meta.requiresAuth) && !auth.currentUser){
    next('/login')
    return;
  }
  next();
})
export default router
