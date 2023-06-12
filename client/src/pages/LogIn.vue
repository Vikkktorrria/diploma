<template>
  <div class="container-wrapper container">

    <section class="content col-lg-8 mx-auto">

      <log-in-form class="log-form"
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
.content{
  width: 850px; /* Здесь вы можете указать нужную ширину */
  height: 600px; /* Здесь вы можете указать нужную высоту */
  border-radius: 20px; /* Здесь вы можете настроить радиус скругления */
  background: #fcfcfc;
  display: flex;
  align-items: center; /* Выравнивание по вертикали */
  flex-direction: column;
  justify-content: flex-start;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.log-form{
  margin-top: 130px;
}
</style>