<template>
  <div class="change_data_modal_table">
    <div class="change_data_header_table">Редактирование дисциплины</div>
    <p><strong>Код:</strong><input :value="this.discipline.discipline_code"></p>
    <p><strong>Название:</strong><input :value="this.discipline.discipline_name"></p>
    <p><strong>Модуль:</strong><input :value="this.discipline.module_name"></p>
    <p><strong>Начало преподавания (семестр):</strong><input :value="this.discipline.taught_per_semester"></p>
    <details>
      <summary><strong>Компетенции</strong></summary>
      <div  class="change_data_accordion_content"
           v-for="comp in all_competences"
           :key="comp.competence_code"
      ><p>
        <input
            type="checkbox"
            :checked="isDisciplineInTrajectory(comp.competence_code)"
            @change="toggleDisciplineSelection(comp.competence_code)"
        >
        {{ comp.competence_code }}
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
    async fetchCompetenses() { // функция для получения данных с сервера
      try {
        const response = await axios.get('/competenses/all');
        this.all_competences = response.data;
        this.selected_competences = this.discipline.competences;
        console.log(this.all_competences)
      } catch (e) {
        alert('Ошибка получения компетенций');
      }
    },
  },
  mounted(){
    this.fetchCompetenses();
    console.log(this.student);
  },
}
</script>

<style scoped>

</style>