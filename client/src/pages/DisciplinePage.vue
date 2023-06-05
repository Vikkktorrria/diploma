<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
    <disciplines-form v-if="this.user.role_id === 2"
        v-bind:elective_disciplines="elective_disciplines"
    />

      <div v-if="this.user.role_id === 1"
      >
        <table class="data_table">
          <thead>
          <tr class="header_row">
            <th>Код</th>
            <th>Начало преподавания (семестр)</th>
            <th>Название</th>
            <th>Модуль</th>
            <th>Компетенции</th>
          </tr>
          </thead>
          <tbody>
          <tr class="content_row"
              v-for="disc in all_disciplines"
              :key="disc.discipline_code"
              @click="showDialog(disc)">
            <td>{{ disc.discipline_code }}</td>
            <td>{{ disc.taught_per_semester }}</td>
            <td>{{ disc.discipline_name }}</td>
            <td>{{ disc.module_name }}</td>
            <td>
                <div
                    v-for="comp in disc.competences"
                    :key="comp.competence_code"
                ><p>{{comp.competence_code}}</p>
                </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>


      <modal-window v-model:show="dialogVisible">
        <discipline-table :discipline="selectedDiscipline"/>
      </modal-window>



    </section>


  </div>
</template>

<script>
import DisciplinesForm from "@/components/DisciplineForm";
import axios from "axios";
import {mapGetters} from "vuex";
import ModalWindow from "@/components/ModalWindow";
import DisciplineTable from "@/components/Tables/DisciplineTable";

export default {
  computed:{
    ...mapGetters(['getUser']),
    user(){
      return this.$store.getters.getUser; // Получение данных пользователя из геттера
    }
  },
  data(){
    return{
      all_disciplines: [],
      elective_disciplines: [],
      dialogVisible: false,
      selectedDiscipline: null,
    }
  },
  name: "disciplines-page",
  components: {
    DisciplineTable,
    ModalWindow,
    DisciplinesForm,
  },
  methods:{
    async fetchAllDisciplines() { // функция для получения данных с сервера
      try{
        const response = await axios.get('/disciplines/all');
        this.all_disciplines = response.data;
      } catch(e){
        alert('Ошибка получения дисциплин');
      }
    },
    showDialog(discipline) {
      console.log('вонючее модальное окно откройся')
      this.dialogVisible = true;
      this.selectedDiscipline = discipline;
    },
    async fetchElectiveDisciplines() { // функция для получения данных с сервера
      try{
        const response = await axios.get('disciplines');
        this.elective_disciplines = response.data;
      } catch(e){
        alert('Ошибка получения дисциплин');
      }
    },
  },
  mounted(){
    this.fetchAllDisciplines();
    this.fetchElectiveDisciplines();
    console.log('дисциплины получаются');
  },
}
</script>

<style scoped>

</style>