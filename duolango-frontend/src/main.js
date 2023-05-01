import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { auth } from './firebase'
import db from "./firebaseInit";
import {collection, addDoc, setDoc, doc, getDoc} from 'firebase/firestore'
import 'firebase/firestore';


const app = createApp(App)

app.config.globalProperties.global = {
    lang: 'Spanish',
    score: 0
}
console.log(app.config.globalProperties.global.score)


app.config.globalProperties.globalLang = {
    async score_retrieve(){
        if(auth.currentUser){
            const docSnap = await getDoc(doc(db, 'users', auth.currentUser.uid))
            if(docSnap.exists()){
                if(app.config.globalProperties.global.lang == 'Spanish'){
                   app.config.globalProperties.global.score = docSnap.data().spanish_score
                   setDoc(doc(db, 'users', auth.currentUser.uid),{swahili_score:docSnap.data().swahili_score, spanish_score:app.config.globalProperties.global.score, current_languge:"Spanish"})
                }else{
                    app.config.globalProperties.global.score = docSnap.data().swahili_score
                    setDoc(doc(db, 'users', auth.currentUser.uid),{swahili_score:docSnap.data().swahili_score, spanish_score:app.config.globalProperties.global.score, current_languge:"Swahili"})
                    }
            }else{
                await setDoc(doc(db, 'users', auth.currentUser.uid),{swahili_score:0, spanish_score:0, current_languge:"None"})
            }
            return app.config.globalProperties.global.score
        
        }
    },
    async score_update(){
        if(auth.currentUser){
            const docSnap = await getDoc(doc(db, 'users', auth.currentUser.uid))
            if(docSnap.exists()){
                if(app.config.globalProperties.global.lang == 'Spanish'){
                    setDoc(doc(db, 'users', auth.currentUser.uid),{swahili_score:docSnap.data().swahili_score, spanish_score:app.config.globalProperties.global.score, current_languge:docSnap.data().current_languge})
                }else{
                    setDoc(doc(db, 'users', auth.currentUser.uid),{swahili_score:app.config.globalProperties.global.score, spanish_score:docSnap.data().spanish_score, current_languge:docSnap.data().current_languge})
                    
                    }
            }else{
                setDoc(doc(db, 'users', auth.currentUser.uid),{swahili_score:0, spanish_score:0})
            }
        
        }
    },    
    changeLang(num){
        if(num == 1){
            app.config.globalProperties.global.lang = 'Spanish'
            //console.log(app.config.globalProperties.global.lang)
        }
        if(num ==0){
            return app.config.globalProperties.global.lang
        }
        if (num > 1){
            app.config.globalProperties.global.lang = 'Swahili'
        }
        this.score_retrieve()
        return app.config.globalProperties.global.lang
    }
};

app.use(store).use(router).mount('#app')
