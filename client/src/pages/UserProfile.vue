<template>
  <body>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">

      <user-form
          v-bind:current_user="current_user"
      />

      <footer class="footer row">

      </footer>

    </section>


  </div>
  </body>
</template>

<script>

import axios from 'axios';
import UserForm from "@/components/Profile/UserForm";

export default {
  data(){
    return{
      current_user: {},
    }
  },
components: {
    UserForm,
  },
  methods:{
    async get_posts() { // функция для получения данных с сервера
      try{
        const response = await axios.get('cur_us');
        this.current_user = response.data;
        console.log(response)
      } catch(e){
        alert('Ошибка');
      }
    },
  },
  mounted(){
    this.get_posts();
    console.log('я лох');
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
