import { createRouter, createWebHistory } from 'vue-router'
import home from '../views/home.vue'
// import {auth} from '../firebase'
import Login from '../views/login.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: home,
  },
  {
    path: '/definer',
    name: 'definer',
    component: () => import(/* webpackChunkName: "about" */ '../views/definer.vue'),
  },
  {
    path: '/tensify',
    name: 'tensify',
    component: () => import(/* webpackChunkName: "about" */ '../views/tensify.vue'),
  },
  {
    path: '/puzzler',
    name: 'puzzler',
    component: () => import(/* webpackChunkName: "about" */ '../views/puzzler.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   if(to.path === '/login' && auth.currentUser){
//     next('/')
//     return;
//   }
//   if(to.matched.some(record => record.meta.requiresAuth) && !auth.currentUser){
//     next('/login')
//     return;
//   }
//   next();
// })
export default router
