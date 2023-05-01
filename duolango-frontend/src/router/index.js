import { createRouter, createWebHistory } from 'vue-router'
import home from '../views/home.vue'
import {auth} from '../firebase'
import Login from '../views/login.vue'
import db from "../firebaseInit";
import {collection, addDoc, setDoc, doc, getDoc} from 'firebase/firestore'
import 'firebase/firestore';
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
    path: '/definer',
    name: 'definer',
    component: () => import(/* webpackChunkName: "about" */ '../views/definer.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/tensify',
    name: 'tensify',
    component: () => import(/* webpackChunkName: "about" */ '../views/tensify.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/puzzler',
    name: 'puzzler',
    component: () => import(/* webpackChunkName: "about" */ '../views/puzzler.vue'),
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

async function score_retrieve(){
  if(auth.currentUser){
      const docSnap = await getDoc(doc(db, 'users', auth.currentUser.uid))
      if(docSnap.exists()){
          if(docSnap.data().current_languge == 'Spanish'){
             return docSnap.data().spanish_score
          }else{
              return docSnap.data().swahili_score
              }  
  }
}
}

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
  if(to.path == '/tensify' && auth.currentUser){
    const myPromise = score_retrieve();
    myPromise.then(result => { if(result >= 50){
      next();
    }else{
      alert('You need 50 points to unlock tensify....loser')
    }}
      );
    return;
  }
  if(to.path == '/puzzler'){ //call to firebase and check score
    const myPromise = score_retrieve();
    myPromise.then(result => { if(result >= 100){
      next();
    }else{
      alert('You need 100 points to unlock tensify....sucker')
    }}
      );
    return;
  }
  next();
})

export default router
