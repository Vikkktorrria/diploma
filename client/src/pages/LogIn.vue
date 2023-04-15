<template>
  <body>
  <div class="container-wrapper container">

    <section class="content col-lg-8 mx-auto">

      <log-in-form/>

      <footer class="footer row">

      </footer>

    </section>


  </div>
  </body>
</template>

<script>
import LogInForm from "@/components/LogInForm";
import axios from "axios";
export default {
  name: "log-in",
  components: {
    LogInForm,
  },
  methods:{
    async get_posts() { // функция для получения данных с сервера
      try{
        const response = await axios.get('login');
        this.current_user = response.data;
        console.log(response)
      } catch(e){
        alert('Ошибка');
      }
    },
  },
}
</script>

<style scoped>

</style>