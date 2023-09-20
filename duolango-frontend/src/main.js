import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store'
const app = createApp(App);

app.config.globalProperties.global = {
    lang: 'Spanish',
}
console.log(app.config.globalProperties.global.score)


app.config.globalProperties.globalLang = {
    changeLang(num){
        if(num == 1){
            app.config.globalProperties.global.lang = 'Spanish'
            console.log(app.config.globalProperties.global.lang)
        }
        
        if (num > 1){
            app.config.globalProperties.global.lang = 'Swahili'
        }
        return app.config.globalProperties.global.lang
    }
};

app.use(router).mount('#app')
