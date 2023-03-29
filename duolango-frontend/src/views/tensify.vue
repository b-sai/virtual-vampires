<template>
  <div>
    <button @click="startGame" v-if="!gameStarted" class="button">Start Game</button>
    <div v-else>
      <h1>{{sentence}} (to {{ verb }}).</h1>
      <button v-for="(option, index) in verbOptions" :key="index" @click="checkVerb(option)" :disabled="feedback == 'Correct!'" class="button">{{ option }}</button>
      
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
    const sentence = ref('');
    const verb = ref('');
    const selectedVerb = ref('');
    const verbOptions = ref([]);
    const correct = ref('')
    const feedback = ref('')

    const makeApiRequest = () => {
      var axios = require('axios');
      var config = {
        method: 'get',
        url: "http://127.0.0.1:8000/en_es_verbs/",
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

  const startGame = async () => {
    gameStarted.value = true;

    const { data } = await makeApiRequest();
    sentence.value = data.sentence;
    verb.value = data.verb;
    verbOptions.value = data.wrong
    correct.value = data.correct
    selectedVerb.value = '';

    // Add the correct verb option
    verbOptions.value.push(data.correct);

    // Shuffle the options
    shuffleArray(verbOptions.value);
  };

  const checkVerb = (verbOption) => {
    if (verbOption === correct.value) {
      selectedVerb.value = verbOption;
      feedback.value = 'Correct!'
      sentence.value = sentence.value.replace('____', correct.value);
      setTimeout(() => {
        startGame();
        feedback.value = '';
      }, 1000); // wait for 1 second before reloading the game and clearing the feedback
    } else {
      selectedVerb.value = verbOption;
      feedback.value = 'Incorrect!'
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
    feedback,
    gameStarted,
    sentence,
    correct,
    verb,
    selectedVerb,
    verbOptions,
    startGame,
    checkVerb
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