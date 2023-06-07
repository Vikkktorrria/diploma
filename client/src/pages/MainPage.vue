<template>
  <div class="container-wrapper container">
    <div class="main-container">
      <div class="main-text">
      <b><p class="welcome">Добро пожаловать!</p></b>
        <p class="where-are-you">Вы находитесь на главной странице приложения для поддержки принятия решения по выбору индивидуальной образовательной траектории обучающегося</p>
        <p class="auth-pls">Для начала работы необходимо авторизоваться</p>
        <button class="btn" @click="toLogInPage">Вход</button>

      </div>
    </div>

  </div>

</template>

<script>
export default {
  name: "main-page",
  methods: {
    toLogInPage() {
      this.$router.push({name: 'login'})
    },
  },
}
</script>

<style scoped>
.welcome{
  font-size: 30px;
  align-self: flex-start;
  margin-top: 60px;
}
.where-are-you{
  font-size: 25px;
  align-self: center; /* Расположение посередине */
  margin-top: 40px; /* Отступ сверху для разделения от текста welcome */
}
.auth-pls{
  margin-top: 60px;
  font-size: 22px;
  color: #787778;
}
.main-container{
  width: 850px; /* Здесь вы можете указать нужную ширину */
  height: 600px; /* Здесь вы можете указать нужную высоту */
  border-radius: 20px; /* Здесь вы можете настроить радиус скругления */
  background: #fcfcfc;
  display: flex;
  align-items: center; /* Выравнивание по вертикали */
  flex-direction: column;
  justify-content: flex-start;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

}
.main-text{
  text-align: center;
  padding: 50px;

}
.btn{
  font-size: 20px;
  padding-left: 35px;
  padding-right: 35px;
}
</style>