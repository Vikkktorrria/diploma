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
  methods:{
    userAuth(current_user) {
      console.log('пользователь воняет:', current_user);
      this.current_user = current_user;

      axios.post('/login', {
        username: this.current_user.login,
        password: this.current_user.password
      })
          .then(response => {
            localStorage.setItem('token', response.data.token)
            console.log('токен',response.data.token)
            // Теперь можно отправлять запросы на защищенные маршруты
          })
          .catch(error => {
            console.log(error + 'я немного воняю')
          })
    },
    login() {

    }
  },
}
</script>

<style scoped>

</style>