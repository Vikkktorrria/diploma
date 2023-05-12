<template>
  <body>
  <div class="container-wrapper container">

    <section class="content col-lg-8 mx-auto">

      <log-in-form
          @auth="userAuth"
      ></log-in-form>

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
  data() {
    return {
      current_user: {
        login: '',
        password: '',
      }
    }
  },
  name: "log-in",
  components: {
    LogInForm,
  },
  methods: {
    async userAuth(current_user) {
      this.current_user = current_user;
      try {
        const response = await axios.post('/login', {
          username: this.current_user.login,
          password: this.current_user.password
        })
        localStorage.setItem('token', response.data.token);
        console.log('токен', response.data.token);
        this.$router.push({name: 'disciplines'})
      } catch (error) {
        console.log(error, error.response.status)
        if (error.response.status === 401) {
          console.log('Неверный логин или парольиус')
        }
      }
    }
  }
}
</script>

<style scoped>

</style>