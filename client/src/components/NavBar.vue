<template>
  <button
      @click="logOut"
  >
    Выход
  </button>
  <div  v-if="this.user.role_id === 1">
    <nav class="my_nav_bar nav-tabs col-lg-5 mx-auto">
      <router-link to="/student/all" class="my_nbar_link nav-link active" aria-current="page">Студенты</router-link>
      <router-link to="/disciplines" class="my_nbar_link nav-link ">Дисциплины</router-link>
      <router-link to="/trajectory" class="my_nbar_link nav-link ">Траектории</router-link>
      <router-link to="#" class="my_nbar_link nav-link">Настройки</router-link>
    </nav>
  </div>

  <div v-else-if="this.user.role_id === 2">
    <nav class="my_nav_bar nav-tabs col-lg-5 mx-auto">
      <router-link to="/profile" class="my_nbar_link nav-link active" aria-current="page">Профиль</router-link>
      <router-link to="/disciplines" class="my_nbar_link nav-link ">Дисциплины</router-link>
      <router-link to="/trajectory" class="my_nbar_link nav-link ">Траектории</router-link>
      <router-link to="#" class="my_nbar_link nav-link">Настройки</router-link>
    </nav>
  </div>

</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  computed:{
    ...mapGetters(['getUser']),
    user() {
      return this.$store.getters.getUser; // Получение данных пользователя из геттера
    },
  },
  name: "nav-bar",
  methods: {
    ...mapActions(['logOutUser']),

    async logOut() { // функция для получения данных с сервера
      this.$store.dispatch('logOutUser'); //сохраняю в локальный стор данные
      this.$router.push({name: 'login'})

    },
  },
  mounted(){
    console.log(this.user.role_id);
  },
}
</script>

<style scoped>

</style>