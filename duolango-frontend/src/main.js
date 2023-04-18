import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

const app = createApp(App)
app.config.globalProperties.global = {
    lang: 'Spanish'
}


app.config.globalProperties.globalLang = {
    changeLang(num){
        if(num == 1){
            return app.config.globalProperties.global.lang = 'Spanish'
        }
        if(num ==0){
            return app.config.globalProperties.global.lang
        }
        else{
            return app.config.globalProperties.global.lang = 'Swahili'
        }
    }
};

app.use(store).use(router).mount('#app')
