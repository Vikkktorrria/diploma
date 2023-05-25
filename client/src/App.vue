<template>
  <div class="app">
    <nav-bar v-if="isAuth"></nav-bar>
    <router-view></router-view>
  </div>
  <div class="container-wrapper container">

  </div>
</template>



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
<script>
import axios from "axios";
axios.defaults.baseURL = 'http://localhost:5000';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
import NavBar from "@/components/NavBar";
import {mapGetters} from "vuex";
export default {
  components: {NavBar},
  computed: {
    ...mapGetters(['isAuth'])
  },
};
</script>