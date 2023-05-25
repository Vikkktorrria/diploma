<template>
  <body>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">

      <user-form></user-form>

      <footer class="footer row">

      </footer>

    </section>


  </div>
  </body>
</template>

<script>

import UserForm from "@/components/Profile/UserForm";

export default {
components: {
    UserForm,
  },
  mounted(){
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
