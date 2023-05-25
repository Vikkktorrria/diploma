<template>
  <div class="profile_item row-cols-1">
    <div class="user-card col-7 mx-auto"> <!-- элемент с фото и фио пользователя (mx-auto) выравнивает элементы посередине -->
      <div class="card user">
        <div class="card-body">
          <img class="card_user_image" src="img/ico.png" alt="иконка">
          <div class="card-title">{{ this.user.name }}
          </div>
        </div>
      </div>
    </div>
    <div class="user-num col-7 mx-auto"> <!-- элемент с номером зачётной книжки -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Номер зачётной книжки студента</h5>
          {{ this.user.rec_book_num }}
        </div>
      </div>
    </div>
    <div class="user-email col-7 mx-auto"> <!-- элемент с почтой -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Почта студента</h5>
          {{ this.user.e_mail }}
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  computed: {
    ...mapGetters(['getUser']),
    user() {
      return this.$store.getters.getUser; // Получение данных пользователя из геттера
    },
  },
  name: "user-form",
  components: {}
}
</script>

<style scoped>

</style>