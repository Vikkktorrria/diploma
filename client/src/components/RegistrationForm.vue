<template>
  <div class="login_form_elem col-7 mx-auto">
    <form @submit.prevent="studentRegistrationData">
      <div class="form__el">
        <input
            v-model="student.surname"
            class="form__input"
            placeholder="Фамилия"
        >
      </div>
      <div class="form__el">
        <input
            v-model="student.name"
            class="form__input"
            placeholder="Имя"
        >
      </div>
      <div class="form__el">
        <input
            v-model="student.patronymic"
            class="form__input"
            placeholder="Отчество"
        >
      </div>
      <div class="form__el">
        <input
            v-model="student.record_book_number"
            class="form__input"
            placeholder="Номер зачётной книжки"
        >
      </div>
      <div class="form__el">
        <input
            v-model="student.e_mail"
            class="form__input"
            placeholder="Почта"
        >
      </div>
      <div class="form__el">
        <input
            v-model="student.login"
            class="form__input"
            placeholder="Логин"
        >
      </div>
      <div class="form__el">
        <input
            v-model="student.password"
            type="password"
            class="form__input"
            placeholder="Пароль"
        >
      </div>
      <div class="form__button">
        <button type="submit" class="btn"
        >
          Зарегистрировать
        </button>
      </div>
    </form>

  </div>
</template>

<script>
export default {
  name: "registration-form",
  data() {
    return{
      student: {
        surname: '',
        name: '',
        patronymic: '',
        record_book_number: '',
        e_mail: '',
        login: '',
        password: '',
      },
    }
  },
  methods: {
    studentRegistrationData(){
      this.$emit('registr', this.student)
    }
  }
}
</script>


<style scoped>
.form .error small {
  display: block;
  color: #e74c3c;
}
.form__el {
  margin-top: 25px;
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
}
.form__input {
  background-color: transparent;
  border: none;
  outline: none;
  border-bottom: 2px solid #f0f0f0;
  padding: 15px 20px;
  margin-bottom: 10px;
  font-size: 20px;
  color: #35538d;
}
</style>