<template>
  <div class="user-card col-7 mx-auto"> <!-- элемент с фото и фио пользователя (mx-auto) выравнивает элементы посередине -->
    <div class="card user">
      <div class="card-body">
        <img class="card_user_image" src="img/ico.png" alt="иконка">
        <div class="card-title">Имя Фамилия отчество
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "user-card",
}
</script>

<style scoped>

</style>