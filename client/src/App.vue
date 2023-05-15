<template>
  <div class="app">
    <nav-bar v-if="isAuth"></nav-bar>
    <router-view></router-view>
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
import NavBar from "@/components/NavBar";
import {mapGetters} from "vuex";
export default {
  components: {NavBar},
  computed: {
    ...mapGetters(['isAuth'])
  },
};
</script>