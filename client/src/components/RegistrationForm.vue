<template>
  <div class="login_form_elem col-7 mx-auto">
    <form>
      <div class="form__el">
        <input
            v-model="student.full_name"
            class="form__input"
            placeholder="ФИО"
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
        <button
            class="btn"
            @click="addStudent"
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
        full_name: '',
        record_book_number: '',
        e_mail: '',
        login: '',
        password: '',
      },
      full_name: '',
      record_book_number: '',
      e_mail: '',
      login: '',
      password: '',
    }
  },
  methods: {
    addStudent(){
      const newStudent = {
        full_name: this.full_name,
        record_book_number: this.record_book_number,
        e_mail: this.e_mail,
        login: this.login,
        password: this.password,
      }
      console.log('Студент зарегистрирован', newStudent)
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