<template>
  <div class="change_data_modal_table">
    <div class="change_data_header_table">Редактирование траектории</div>
    <p><strong>Номер траектории:</strong><input :value="this.trajectory.trajectory_id" class="table_data_input disabled" disabled></p>
    <p><strong>Код специальности:</strong><input :value="this.trajectory.speciality_code" class="table_data_input"></p>
    <p><strong>Название специальности:</strong><input :value="this.trajectory.speciality_name" class="table_data_input"></p>
    <details>
      <summary><strong>Дисциплины</strong></summary>
      <div
          v-for="dics in selected_disciplines"
          :key="dics.discipline_code"
      ><p class="mark_list_in_table">
       <!-- <input
          type="checkbox"
          :checked="isDisciplineInTrajectory(dics.discipline_code)"
          @change="toggleDisciplineSelection(dics.discipline_code)"
        > -->
        • {{ dics.discipline_name}}
      </p></div>
    </details>

  </div>
  <button class="btn">Сохранить</button>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      all_disciplines: [],
      selected_disciplines: [],
    }
  },
  name: "trajectory-table",
  props: {
    trajectory: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async fetchDisciplines() { // функция для получения данных с сервера
      try{
        const response = await axios.get('/disciplines/all');
        this.all_disciplines = response.data;
        this.selected_disciplines = this.trajectory.disciplines;
        console.log(this.all_disciplines)
      } catch(e){
        alert('Ошибка получения дисциплин');
      }
    },
    isDisciplineInTrajectory(disciplineId) {
      if (this.selected_disciplines.some(selected_disciplines => selected_disciplines.discipline_code === disciplineId)) {
        console.log('Match found');
        return true;
      //return this.selectedDisciplines.includes(disciplineId);
      }
    },
    toggleDisciplineSelection(disciplineId) {
      const index = this.selected_disciplines.indexOf(disciplineId);
      if (index === -1) {
        this.selected_disciplines.push(disciplineId);
      } else {
        this.selected_disciplines.splice(index, 1);
      }
    },
  },
  mounted(){
    console.log(this.trajectory)
    this.fetchDisciplines()
  },
}

</script>

<style scoped>

</style>