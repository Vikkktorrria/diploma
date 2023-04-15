<template>
  <nav class="my_nav_bar nav-tabs col-lg-5 mx-auto">
    <router-link to="/profile" class="my_nbar_link nav-link" aria-current="page">Профиль</router-link>
    <router-link to="/disciplines" class="my_nbar_link nav-link ">Дисциплины</router-link>
    <router-link to="/trajectory" class="my_nbar_link nav-link active">Траектории</router-link>
    <router-link to="#" class="my_nbar_link nav-link">Настройки</router-link>
  </nav>

</template>

<script>
export default {
  name: "nav-bar"
}
</script>

<style scoped>

</style>