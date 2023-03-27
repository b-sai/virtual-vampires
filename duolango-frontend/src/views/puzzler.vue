<template>
  <div class="game1">
    <div>
        <p>Translate the sentence: "I walk to school"</p>
        <p>{{ sentence }}</p>
        <button v-for="answer in answers" :key="answer.text" @click="checkAnswer(answer)">{{ answer.text }}</button>
        <p v-if="selectedAnswer !== ''">{{ isAnswerCorrect ? 'Correct!' : 'Incorrect!' }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
export default {
  name: 'Game',
  setup() {
    const sentence = ref('___ ___ ___ ___ ___');
    const answers = ref([
      { text: 'Yo', isCorrect: true },
      { text: 'camino', isCorrect: true },
      { text: 'a', isCorrect: true },
      { text: 'la', isCorrect: true },
      { text: 'escuela', isCorrect: true },
    ]);
    const selectedAnswer = ref('');
    const isAnswerCorrect = ref(false);
    const checkAnswer = (answer) => {
      selectedAnswer.value = answer.text;
      isAnswerCorrect.value = answer.isCorrect;
      if (isAnswerCorrect.value) {
        sentence.value = sentence.value.replace('___', selectedAnswer.value);
      }
    }
    return {
      sentence,
      answers,
      selectedAnswer,
      isAnswerCorrect,
      checkAnswer,
    };
  },
};
</script>

<style>
  button {
    margin: 5px;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
  }
  p {
    font-size: 20px;
  }
</style>