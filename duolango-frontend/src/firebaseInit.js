// src/firebaseInit.js
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.VUE_APP_apiKey,
  authDomain: process.env.VUE_APP_authDomain ,
  databaseURL:process.env.VUE_APP_databaseURL ,
  projectId: process.env.VUE_APP_projectId,
  storageBucket: process.env.VUE_APP_storageBucket,
  messagingSenderId: process.env.VUE_APP_storageBucket,
  appId: process.env.VUE_APP_appId
};


initializeApp(firebaseConfig)
// Initialize Firebase
const db = getFirestore()
export default db;