<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
      <button class="btn"  @click="$router.push({name: 'studentRegistration'})">Регистрация студентов</button>
      <table>
        <thead>
        <tr class="header_row">
          <th>Номер зачётной книжки</th>
          <th>Фамилия</th>
          <th>Имя</th>
          <th>Отчество</th>
          <th>Эл.почта</th>
        </tr>
        </thead>
        <tbody>
        <tr class="content_row"
            v-for="student in all_students"
            :key="student.user_id"
            @click="showDialog(student)">
          <td>{{ student.record_book_number }}</td>
          <td>{{ student.surname }}</td>
          <td>{{ student.name }}</td>
          <td>{{ student.patronymic }}</td>
          <td>{{ student.e_mail }}</td>
        </tr>
        </tbody>
      </table>
      <modal-window
          v-model:show="dialogVisible"
      >
        <student-table
            @changeData="changeStudentData"
            :student="selectedStudent"
        />

      </modal-window>

    </section>


  </div>
</template>

<script>
import axios from "axios";
import StudentTable from "@/components/Tables/StudentTable";
import ModalWindow from "@/components/ModalWindow";

export default {
  components: {
    StudentTable,
    ModalWindow
  },
  data(){
    return{
      all_students: [],
      dialogVisible: false,
      selectedStudent: null,
    };
  },
  name: "student-page",
  methods:{
    async fetchStudents() { // функция для получения данных с сервера
      try{
        const response = await axios.get('/student/all');
        this.all_students = response.data;
        console.log(response)
      } catch(e){
        alert('Ошибка');
      }
    },
    showDialog(student) {
      this.dialogVisible = true;
      this.selectedStudent = student;
    },
    async changeStudentData(dataFromChild){
      console.log(dataFromChild);

    }


  },
  mounted(){
    this.fetchStudents();
  },
}
</script>

<style scoped>

</style>