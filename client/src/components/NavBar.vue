<template>


  <div class="exit_btn col-lg-8 mx-auto">
    <img @click="logOut" src="../assets/exit_ico_mini.png"><b>Выход</b>
  </div>

  <div  v-if="this.user.role_id === 1">
    <nav class="my_nav_bar nav-tabs col-lg-5 mx-auto">
      <router-link to="/student/all" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/student/all' }]" aria-current="page">Студенты</router-link>
      <router-link to="/disciplines" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/disciplines' }]">Дисциплины</router-link>
      <router-link to="/trajectory" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/trajectory' }]">Траектории</router-link>
      <router-link to="/competence" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/competence' }]">Компетенции</router-link>
      <router-link to="/settings" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/settings' }]">Настройки</router-link>
    </nav>
  </div>

  <div v-else-if="this.user.role_id === 2">
    <nav class="my_nav_bar nav-tabs col-lg-5 mx-auto">
      <router-link to="/profile" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/profile' }]" aria-current="page">Профиль</router-link>
      <router-link to="/disciplines" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/disciplines' }]">Дисциплины</router-link>
      <router-link to="/trajectory" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/trajectory' }]">Траектории</router-link>
      <router-link to="/competence" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/competence' }]">Компетенции</router-link>
      <router-link to="/settings" :class="['my_nbar_link', 'nav-link', { active: $route.path === '/settings' }]">Настройки</router-link>
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
      this.$store.dispatch('logOutUser');
      this.$router.push({name: 'login'})

    },
  },
  mounted(){
    console.log(this.user.role_id);
  },
}
</script>

<style scoped>
.exit_btn{
  cursor: pointer;
  text-align: right;
  width: 45%;
  margin-bottom: 20px;
}
.my_nav_bar{

}
.navigation_bar, .nav{
  text-align: center;
  white-space: nowrap;

}
.navigation_el{
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  padding: 15px 10px;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  transition-duration: .4s;
  border: 1px solid;
  border-right-style: none;
  color: black;

}

.nav-tabs {
  text-align: center;
  --bs-nav-tabs-border-color: transparent;
  border-color: transparent;
  margin-bottom: -1px;
}

.nav-link {
  float: none;
  display: inline-block;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 20px;
}
.nav-link.active{
  background-color: #fcfcfc;
}
</style>