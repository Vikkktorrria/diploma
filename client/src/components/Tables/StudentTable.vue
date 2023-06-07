<template>
    <div class="change_data_modal_table">
      <div class="change_data_header_table">Редактирование студента</div>
      <p class="table_item"><strong>Номер <br>зачётной <br> книжки:</strong><input :value="this.student.record_book_number" class="table_data_input disabled" disabled></p>
      <p class="table_item"><strong>Фамилия:</strong><input v-model="local_student.surname" class="table_data_input"></p>
      <p class="table_item"><strong>Имя:</strong><input :value="this.student.name" class="table_data_input"></p>
      <p class="table_item"><strong>Отчество:</strong><input :value="this.student.patronymic" class="table_data_input"></p>
      <p class="table_item"><strong>Эл.почта:</strong><input :value="this.student.e_mail" class="table_data_input"></p>
    </div>
  <button class="btn" @click="sendNewData">Сохранить</button>
</template>

<script>

export default {
  name: "student-table",
  props: {
    student: {
      record_book_number: '',
      surname: '',
      name: '',
      patronymic: '',
      e_mail:'',
    },
  },
  data(){
    return{
      local_student: this.student
    }
  },
  mounted(){
    console.log(this.student)
  },
  methods:{
    sendNewData() {
      this.$emit('changeData', this.student)
    },


  }
}

</script>

<style scoped>

</style>