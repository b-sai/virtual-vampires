<template>
  <div>
    <p>Piece together the sentence (if Swahili, remember it's one word broken apart)!</p>
    <br>
    <button @click="startGame" v-if="!gameStarted" class="button">Start Game</button>
    <div v-else>
      <h1>Translate: {{ sentence }}</h1>
      <br>
      
      <div class="sequence-buttons">
        <button v-for="(word, index) in wordSequence" :key="index" @click="removeWord(index)" class="button sentence-word">{{ word }}</button>
        
      </div>
      
      <hr style="width:40%">
     <div class="word-buttons">
      <button v-for="(option, index) in verbOptions" :key="index" @click="addWord(option)" 
              :disabled="isWordSelected(option)" class="button">{{ option }}</button>
      </div>
      
      <button @click="submitAnswer" class="button button-submit" :disabled="wordSequence.length !== verbOptions.length">Submit</button>
      
      <h2>{{ feedback }}</h2>
    </div>
    <p>Language: {{global.lang}}</p>
    <br>
    <br>
    <br>
    <br>
    <br>
    <hr>
    <p>Struggling?</p>
    <p>Here are some resources to help:</p>

    <a href="https://www.swahilicheatsheet.com/" target="_blank">Swahili Cheat Sheet</a>
    <br>
    <br>
    <a href="https://www.dummies.com/article/academics-the-arts/language-language-arts/learning-languages/spanish/spanish-verbs-for-dummies-cheat-sheet-209434/" target="_blank">Spanish Cheat Sheet</a>
  </div>
</template>

<script>
import { ref, getCurrentInstance } from 'vue';
export default {
  data() {
        return {
            myVar: this.globalVar
        }
    },
  name: 'Game',
  setup() {
    const gameStarted = ref(false);
    const sentence = ref('');
    const verbOptions = ref([]);
    const wordSequence = ref([]);
    const selectedVerb = ref('');
    const correctSequence = ref([]);
    const feedback = ref('');
    const { proxy } = getCurrentInstance();

    const makeApiRequest = () => {
      var axios = require('axios');
      var apiLink = ('')
      if (proxy.global.lang == "Spanish"){
        apiLink = "http://127.0.0.1:8000/en_es_sent/"
      }
      else{
        apiLink = "http://127.0.0.1:8000/en_swa_sent/"
      }
      var config = {
        method: 'get',
        url: apiLink,
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

    const isWordSelected = (word) => {
      return wordSequence.value.includes(word);
    };

    const startGame = async () => {
      gameStarted.value = true;

      const { data } = await makeApiRequest();

      sentence.value = data.en;
      verbOptions.value = data.foreign;
      correctSequence.value = [...data.foreign];

      
  
      shuffleArray(verbOptions.value);
    };

    const addWord = (word) => {
      if (wordSequence.value.length < verbOptions.value.length) {
        wordSequence.value.push(word);
      }
    };
    
    const removeWord = (index) => {
      wordSequence.value.splice(index, 1);
    };
    
    const submitAnswer = () => {
      if (JSON.stringify(wordSequence.value) === JSON.stringify(correctSequence.value)) {
        
        feedback.value = 'Correct!';
        setTimeout(() => {
          startGame();
          wordSequence.value = [];
          feedback.value = '';
        }, 1000);
      } else {
        feedback.value = 'Incorrect!';
        
      }
    };

    const shuffleArray = (array) => {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    };

    return {
      feedback,
      gameStarted,
      sentence,
      verbOptions,
      wordSequence,
      selectedVerb,
      correctSequence,
      isWordSelected,
      startGame,
      addWord,
      removeWord,
      submitAnswer,
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

.button-submit {
  background-color: #008CBA; /* Blue */
}

.word-buttons {
  margin-top: 20px;
}

.word-buttons .button {
  background-color: #555555;
  color: white;
}

.hr {
  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1px;
}
.sentence-word {
  font-weight: bold;
}
</style>