<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/definer">Definer</router-link> |
    <router-link to="/tensify">Tensify</router-link> |
    <router-link to="/puzzler">Puzzler</router-link> |
    <!-- <button id="buttons" @click="$store.dispatch('logout')">Logout</button> -->
  </div>
  <router-view />
</template>


<script>
import { defineComponent } from 'vue';
import router from './router';
import { onBeforeMount } from 'vue'
import {useStore} from 'vuex'

export default {
  setup() {
    const store = useStore()
  }
}
// export default defineComponent({
//   name: 'App',
//   router,
// });
</script>


<style>
  #buttons {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 12px 15px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
