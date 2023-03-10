<template>
  <body>
    <div class="container-wrapper container">
    <nav-bar>

    </nav-bar>
      <section class="content col-lg-8 mx-auto">

        <log-in-form />

        <user-form/>

        <footer class="footer row">
          #
        </footer>

      </section>


  </div>
  </body>
</template>

<script>



import NavBar from "@/components/NavBar";
import UserForm from "@/components/Profile/UserForm";
import LogInForm from "@/components/LogInForm";
export default {
  data(){
    return{
      current_user: {
        id: 1,
        login: 'login',
        password:'12334',
        full_name: 'Копыльских Виктория Максимовна',
        rec_book_num: 234323,
        e_mail: 'test@test.ru'
      },
      login: '',
      password: '',
    }
  },
  name: 'App',
  components: {
    LogInForm,
    UserForm,
    NavBar,



  }
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
