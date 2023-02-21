<template>
                      <p>Please create an account and game!</p>
                      <button @click="makeApiRequest">make request</button>
                      <div> English word {{ eng }} | Spanish word {{ spn }}</div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const testing = ref(null);
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
      axios(config)
        .then(function (response) {
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error);
        });
    };

    return {
      makeApiRequest,


    }


  },

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

