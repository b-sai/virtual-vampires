<template>
  <div>
    <button @click="startGame" v-if="!gameStarted" class="button">Start Game</button>
    <div v-else>
      <h1>{{ spanishWord }}</h1>
        <button v-for="(option, index) in translationOptions" :key="index" @click="checkTranslation(option)" :disabled="feedback == 'Correct!'" class="button">{{ option }}</button>
        <h2 v-if="selectedVerb !== ''">{{  feedback }}</h2>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'Game',
  setup() {
    const gameStarted = ref(false);
    const englishWord = ref('');
    const spanishWord = ref('');
    const selectedTranslation = ref('');
    const translationOptions = ref([]);
    const feedback = ref('')

    const makeApiRequest = () => {
      var axios = require('axios');
      var config = {
        method: 'get',
        url: "http://127.0.0.1:8000/rand_elem/",
        auth: {
          username: process.env.VUE_APP_username,
          password: process.env.VUE_APP_password,
        },
        headers: {
          'Content-Type': 'application/json',
        },
      };
      return axios(config);
    };

    const makeIncorrectApiRequest = () => {
      var axios = require('axios');
      var config = {
        method: 'get',
        url: "http://127.0.0.1:8000/rand_elem/",
        auth: {
          username: process.env.VUE_APP_username,
          password: process.env.VUE_APP_password,
        },
        params: {
          sp: spanishWord.value,
          en: false,
        },
        headers: {
          'Content-Type': 'application/json',
        },
      };
      return axios(config);
    };

    const startGame = async () => {
      gameStarted.value = true;

      const { data } = await makeApiRequest();
      englishWord.value = data.en;
      spanishWord.value = data.sp;
      selectedTranslation.value = '';
      
      // Generate three incorrect translation options
      translationOptions.value = [];
      while (translationOptions.value.length < 3) {
        const { data } = await makeIncorrectApiRequest();
        const incorrectOption = data.en;
        if (!translationOptions.value.includes(incorrectOption) && incorrectOption !== englishWord.value) {
          translationOptions.value.push(incorrectOption);
        }
      }
      
      // Add the correct translation option
      translationOptions.value.push(englishWord.value);
      
      // Shuffle the options
      shuffleArray(translationOptions.value);
    };

    const checkTranslation = (translation) => {
      if (translation === englishWord.value) {
        feedback.value = 'Correct!'
        setTimeout(() => {
        startGame();
        feedback.value = '';
      }, 1000);
      } else {
        feedback.value = 'Incorrect!'
        selectedTranslation.value = translation;
      }
    };

    // Shuffle an array in place using the Fisher-Yates algorithm
    const shuffleArray = (array) => {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }

    return {
      gameStarted,
      feedback,
      englishWord,
      spanishWord,
      selectedTranslation,
      translationOptions,
      startGame,
      checkTranslation,
};

  },
};
</script>

<style>
.button {
  font-size: 24px;
  font-weight: bold;
  background-color: #4CAF50;
  color: white;
  padding: 20px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 12px;
  border: none;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3);
  transition: all 0.2s ease-in-out;
}

.button:hover {
  background-color: #3e8e41;
}
</style>