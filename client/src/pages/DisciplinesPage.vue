<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
    <disciplines-form
        v-bind:all_disciplines="all_disciplines"
    />

      <footer class="footer row">

      </footer>

    </section>


  </div>
</template>

<script>
import DisciplinesForm from "@/components/DisciplinesForm";
import axios from "axios";
export default {
  data(){
    return{
      all_disciplines: [],
    }
  },
  name: "disciplines-page",
  components: {
    DisciplinesForm,
  },
  methods:{
    async fetchDisciplines() { // функция для получения данных с сервера
      try{
        const response = await axios.get('disciplines');
        this.all_disciplines = response.data;
      } catch(e){
        alert('Ошибка получения дисциплин');
      }
    },
  },
  mounted(){
    this.fetchDisciplines();
    console.log('дисциплины получаются');
  },
}
</script>

<style scoped>

</style>