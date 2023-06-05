<template>
  <form>
    <div class="row-cols-1">
      <div class="col-7 mx-auto"> <!-- элемент с номером зачётной книжки -->
        <div class="card change_data_card">
          <div class="card-body">
            <h5 class="card-title">Пароль</h5>
            <div class="card_item">
              <label class="card_label">Новый пароль:</label>
              <input
                  v-model="new_password"
                  class="card_input"
                  placeholder="*****"
              >
            </div>

            <div class="card_item">
              <label class="card_label">Повторите пароль:</label>
              <input
                  v-model="repeat_password"
                  class="card_input"
                  placeholder="*****"
              >

            </div>

            <div>
              <button type="submit" class="btn">
                Сохранить
              </button>
            </div>

          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: "password-change-form"
}
</script>

<style scoped>
label{
  display: flex;
}

</style>