// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getAuth} from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCwGC1fvk2vmtNIZ-wyzS8WDPx5g9xA83s",
  authDomain: "worse-duolingo.firebaseapp.com",
  projectId: "worse-duolingo",
  storageBucket: "worse-duolingo.appspot.com",
  messagingSenderId: "562797851309",
  appId: "1:562797851309:web:d9d34341f2cd6e4f400c24"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
export { auth }
