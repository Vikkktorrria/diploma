<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
      <div
          v-for="stud in all_students"
          :key="stud.user_id"
          :stud="stud"
      ></div>
      <footer class="footer row">

      </footer>

    </section>


  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      all_students: [],
    }
  },
  name: "student-page",
  components: {
  },
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
  },
  mounted(){
    this.fetchStudents();
  },
}
</script>

<style scoped>

</style>