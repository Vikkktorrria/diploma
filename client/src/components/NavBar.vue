<template>
  <button
      @click="logOut"
  >
    Выход
  </button>
  <nav class="my_nav_bar nav-tabs col-lg-5 mx-auto">
    <router-link to="/profile" class="my_nbar_link nav-link active" aria-current="page">Профиль</router-link>
    <router-link to="/disciplines" class="my_nbar_link nav-link ">Дисциплины</router-link>
    <router-link to="/trajectory" class="my_nbar_link nav-link ">Траектории</router-link>
    <router-link to="#" class="my_nbar_link nav-link">Настройки</router-link>
  </nav>

</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "nav-bar",
  methods: {
    ...mapActions(['logOutUser']),

    async logOut() { // функция для получения данных с сервера
      this.$store.dispatch('logOutUser'); //сохраняю в локальный стор данные
      this.$router.push({name: 'login'})

    },
  },
}
</script>

<style scoped>

</style>