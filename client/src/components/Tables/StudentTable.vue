<template>
    <div class="change_data_modal_table">
      <div class="change_data_header_table">Редактирование студента</div>
      <p><strong>Фамилия:</strong><input :value="this.student.surname"></p>
      <p><strong>Имя:</strong><input :value="this.student.name"></p>
      <p><strong>Отчество:</strong><input :value="this.student.patronymic"></p>
      <p><strong>Номер зачётной книжки:</strong><input :value="this.student.record_book_number"></p>
      <p><strong>Эл.почта:</strong><input :value="this.student.e_mail"></p>
      <p><strong>Логин:</strong><input :value="this.student.login"></p>
    </div>
  <button class="btn">Сохранить</button>
</template>

<script>
export default {
  name: "student-table",
  props: {
    student: {
      type: Object,
      required: true,
    },
  },
  mounted(){
    console.log(this.student)
  },
}

</script>

<style scoped>
</style>