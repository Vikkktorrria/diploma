<template>
  <div class="profile_item row-cols-1">
    <div class="user-card col-7 mx-auto"> <!-- элемент с фото и фио пользователя (mx-auto) выравнивает элементы посередине -->
      <div class="card user">
        <div class="card-body">
          <img class="card_user_image" src="../assets/user_ico.png" alt="иконка">
          <div class="card-title">{{ this.user.surname }} {{ this.user.name }} {{ this.user.patronymic }}
          </div>
        </div>
      </div>
    </div>
    <div class="col-7 mx-auto"> <!-- элемент с номером зачётной книжки -->
      <div class="card">
        <div class="card-body">
          <div class="card-title user-form">Номер зачётной книжки студента</div>
          <label class="card_label">{{ formattedNumber  }}</label>

        </div>
      </div>
    </div>
    <div class="col-7 mx-auto"> <!-- элемент с почтой -->
      <div class="card">
        <div class="card-body">
          <div class="card-title user-form">Почта студента</div>
          <label class="card_label">{{ this.user.e_mail }}</label>
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
    formattedNumber() {
      const value = this.user.record_book_number .toString();
      return `${value.substr(0, 2)}-${value.substr(2, 2)}-${value.substr(4)}`;
    },
  },
  name: "user-form",
  components: {},
  mounted(){
    console.log(this.user);
  },

}
</script>

<style scoped>

</style>