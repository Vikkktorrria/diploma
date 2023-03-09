<template>
  <body>
    <div class="container-wrapper container">
    <nav-bar>

    </nav-bar>
      <section class="content col-lg-8 mx-auto">

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
export default {
  name: 'App',
  components: {
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
