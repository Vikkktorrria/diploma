<template>
  <div class="login_form_elem col-7 mx-auto">
  <form>
    <div class="form__el">
      <input
          v-model="current_user.login"
          class="form__input"
          placeholder="Логин"
      >
    </div>
    <div class="form__el">
      <input
          v-model="current_user.password"
          type="password"
          class="form__input"
          placeholder="Пароль"
      >
    </div>
    <div class="form__button">
      <button class="btn">
        Войти
      </button>
    </div>
  </form>
</div>
</template>

<script>
export default {
  data() {
    return{
      current_user: {
        login: '',
        password: '',
      }
    }
  },
  name: "log-in-form"
}
</script>

<style scoped>
.form .error small {
  display: block;
  color: #e74c3c;
}
.login_form_elem{
  margin: 100px auto;
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