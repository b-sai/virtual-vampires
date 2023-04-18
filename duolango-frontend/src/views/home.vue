<template>
  <div class="container">
    <h1 class="title">Welcome to Duolango!</h1>
    <p class="subtitle">Our site provides three language learning activities:</p>
    <ul class="activities">
      <li>Definer lets you learn verb vocab by choosing the correct definition.</li>
      <li>Tensify lets you choose the correct verb tense for the sentence.</li>
      <li>Puzzler lets you piece together sentences (if learning Swahili, these sentences will be one word broken apart).</li>
    </ul>
    <p class="description">Games will be unlocked as you gain a foothold in your language of choice, first Definer all the way to Puzzler. This is because each game gives you a new part of the sentence to learn, allowing for growth by progressing through each game!</p>

<p class="progress">Your progress will be tracked via your account.</p>
<h2 class="call-to-action">Choose a Language:</h2>
<div class="language-selector">
  <button class="button" @click="switchToSpanish">Spanish</button>
  <button class="button" @click="switchToSwahili">Swahili</button>
</div>
<p class="selected-language">Selected Language: {{globalLang.changeLang(switchValue)}}</p>
<p class="have-fun">Have fun!</p>

 </div>
</template>
<script>
  import { ref } from 'vue';

  export default {
    setup() {
      const switchValue = ref(0);

      function switchToSpanish() {
        switchValue.value = 1;
      }

      function switchToSwahili() {
        switchValue.value = 2;
      }

      return {
        switchValue,
        switchToSpanish,
        switchToSwahili
      }
    }
  }
</script>
<style>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  .title {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
  }

  .subtitle {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .activities {
    margin-left: 20px;
    margin-bottom: 20px;
    list-style-type: disc;
  }

  .description {
    font-size: 18px;
    line-height: 1.5;
    margin-bottom: 20px;
  }

  .progress {
    font-size: 18px;
    margin-bottom: 20px;
  }

  .call-to-action {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .language-selector {
   display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
margin-bottom: 20px;
}

.button {
font-size: 18px;
padding: 10px 20px;
margin: 0 10px;
border-radius: 5px;
background-color: #3498db;
color: #fff;
cursor: pointer;
transition: all 0.3s ease-in-out;
}

.button:hover,
.button:focus {
background-color: #2980b9;
}

.selected-language {
font-size: 18px;
margin-bottom: 20px;
}

.have-fun {
font-size: 24px;
font-weight: bold;
margin-top: 50px;
text-align: center;
}
</style>