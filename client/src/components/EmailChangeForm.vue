<template>
  <form>
    <div class="row-cols-1">
      <div class="col-7 mx-auto"> <!-- элемент с номером зачётной книжки -->
        <div class="card change_data_card">
          <div class="card-body">
            <h5 class="card-title">Адрес электронной почты</h5>
            <div class="card_item">
            <label class="card_label">Введите почту:</label>
              <input
                    v-model="new_email"
                    class="card_input"
                    placeholder="example@domain.ru"
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
  name: "email-change-form",
  data() {
    return{
      new_email: null,
    }
  },
}
</script>

<style scoped>

</style>