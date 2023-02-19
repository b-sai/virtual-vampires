<template>
                  <p>Please create an account and game ! {{ testing }}</p>
                  <button @click="makeApiRequest">make request</button>
</template>

<script>
import { ref } from 'vue';

console.log("Hello World");

export default {
  setup(){
    const testing = ref(null);

    const makeApiRequest = () => {

      var axios = require('axios');
      var config = {
        method: 'get',
        url: 'https://api.coindesk.com/v1/bpi/currentprice.json',
        headers: {
          'Content-Type': 'application/json',
        },
      };
      axios(config)
        .then(function (response) {
          console.log(response.data)

        })
        .catch(function (error) {
          console.log(error);
        });
    };

    return{
      makeApiRequest,


    }


  }
}
  
</script>
