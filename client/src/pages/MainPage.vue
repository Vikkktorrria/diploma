<template>
  <body>
  <div class="container-wrapper container">

  </div>
  </body>
</template>

<script>
import axios from "axios";
axios.defaults.baseURL = 'http://localhost:5000';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
export default {
  name: "main-page"
}
</script>

<style scoped>

</style>