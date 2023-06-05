<template>
  <div class="change_data_modal_table">
    <div class="change_data_header_table">Редактирование дисциплины</div>
    <p><strong>Код:</strong><input :value="this.discipline.discipline_code" class="table_data_input disabled" disabled></p>
    <p><strong>Начало преподавания (семестр):</strong><input :value="this.discipline.taught_per_semester" class="table_data_input disabled" disabled></p>
    <p><strong>Название:</strong><input :value="this.discipline.discipline_name" class="table_data_input"></p>
    <p><strong>Модуль:</strong><input :value="this.discipline.module_name" class="table_data_input"></p>
    <details>
      <summary><strong>Компетенции</strong></summary>
      <div  class="change_data_accordion_content"
           v-for="comp in selected_competences"
           :key="comp.competence_code"
      ><p class="mark_list_in_table">
       <!-- <input
            type="checkbox"
            :checked="isCompetenceInDiscipline(comp.competence_code)"
        > -->
        • {{ comp.competence_code }}
      </p></div>
    </details>

  </div>
  <button class="btn">Сохранить</button>
</template>

<script>
import axios from "axios";

export default {
  name: "discipline-table",
  data(){
    return{
      all_competences: [],
      selected_competences: [],
    }
  },
  props: {
    discipline: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async fetchCompetences() { // функция для получения данных с сервера
      try {
        const response = await axios.get('/competences/all');
        this.all_competences = response.data;
        this.selected_competences = this.discipline.competences;
        console.log('компетенции получены', this.all_competences)
      } catch (e) {
        alert('Ошибка получения компетенций');
      }
    },
    isCompetenceInDiscipline(competenceId) {
      if (this.selected_competences.some(selected_competences => selected_competences.competence_code === competenceId)) {
        console.log('Match found');
        return true;
        //return this.selectedDisciplines.includes(disciplineId);
      }
    },
  },
  mounted(){
    this.fetchCompetences();
    console.log(this.student);
  },


}
</script>

<style scoped>

</style>