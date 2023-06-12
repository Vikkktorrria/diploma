<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
      <div class="settings-elem" v-if="this.user.role_id === 2">
        <email-change-form></email-change-form>
        <password-change-form></password-change-form>
      </div>
      <div class="settings-elem reg" v-if="this.user.role_id === 1">


        <div class="col-7 mx-auto"> <!-- элемент с номером зачётной книжки -->
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Личная информация</h5>


              <div class="card_item reg">
                <label class="card_label">Электронная почта:</label>
                <p
                    class="card_input"
                >{{this.user.e_mail}}</p>
              </div>


              <div class="card_item reg">
                <label class="card_label">ФИО пользователя:</label>
                <p class="card_input">{{ this.user.surname }} {{ this.user.name }} {{ this.user.patronymic }}</p>
              </div>

            </div>
          </div>
        </div>


        <password-change-form></password-change-form>
      </div>

    </section>
  </div>
</template>

<script>
import EmailChangeForm from "@/components/EmailChangeForm";
import PasswordChangeForm from "@/components/PasswordChangeForm";
import {mapGetters} from "vuex";
export default {
  computed:{
    ...mapGetters(['getUser']),
    user(){
      return this.$store.getters.getUser; // Получение данных пользователя из геттера
    }
  },
  name: "settings-page",
  components: {PasswordChangeForm, EmailChangeForm},
  mounted() {
    console.log(this.user)
  }
}
</script>

<style scoped>
.settings-elem{
  margin-top: 100px;
}
.card_item.reg{

}

</style>