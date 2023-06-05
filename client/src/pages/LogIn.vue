<template>
  <div class="container-wrapper container">

    <section class="content col-lg-8 mx-auto">

      <log-in-form
          @auth="userAuth"
      ></log-in-form>

      <footer class="footer row">

      </footer>

    </section>


  </div>
</template>

<script>
import LogInForm from "@/components/LogInForm";
import axios from "axios";
import {mapActions} from "vuex";

export default {
  data() {
    return {
      current_user: {
        login: '',
        password: '',
      },
    }
  },
  name: "log-in",
  components: {
    LogInForm,
  },
  methods: {
    ...mapActions(['updateUser']),

    async userAuth(current_user) {
      this.current_user = current_user;
      try {
        const response = await axios.post('/login', {
          username: this.current_user.login,
          password: this.current_user.password
        })
        localStorage.setItem('token', response.data.token);

        console.log('токен', response.data.token);
       // console.log('данные пользователя', response.data)

        this.$store.dispatch('updateUser', response.data.user); //сохраняю в локальный стор данные


        if (response.data.user.role_id === 1) {
          this.$router.push({name: 'studentPage'})
        }
        else if (response.data.user.role_id === 2){
          this.$router.push({name: 'profile'})
        }

      } catch (error) {
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