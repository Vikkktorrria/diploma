<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
      <competence-form v-if="this.user.role_id === 2"
                       v-bind:all_competences="all_competences"

      />
      <div v-if="this.user.role_id === 1"
      >
      <table>
        <thead>
        <tr class="header_row">
          <th>Код компетенции</th>
          <th>Тип компетенции</th>
          <th>Описание</th>
        </tr>
        </thead>
        <tbody>
        <tr class="content_row"
            v-for="compenetce in all_competences"
            :key="compenetce.competence_code"
            @click="showDialog(compenetce)">
          <td>{{ compenetce.competence_code }}</td>
          <td>{{ compenetce.type_name }}</td>
          <td>{{ compenetce.description }}</td>
        </tr>
        </tbody>
      </table>
      </div>
      <modal-window
          v-model:show="dialogVisible"
      >
        <competence-table
            :compenetce="selectedCompetence"
        />

      </modal-window>



    </section>


  </div>
</template>

<script>
import axios from "axios";
import ModalWindow from "@/components/ModalWindow";
import CompetenceTable from "@/components/Tables/CompetenceTable";
import CompetenceForm from "@/components/CompetenceForm";
import {mapGetters} from "vuex";

export default {
  computed:{
    ...mapGetters(['getUser']),
    user(){
      return this.$store.getters.getUser; // Получение данных пользователя из геттера
    }
  },
  name: "competence-page",
  components: {CompetenceForm, CompetenceTable, ModalWindow},
  data(){
    return{
      all_competences: [],
      dialogVisible: false,
      selectedCompetence: null,
    };
  },
  methods:{
    async fetchCompetences() { // функция для получения данных с сервера
      try {
        const response = await axios.get('/competences/all');
        this.all_competences = response.data;
        console.log('компетенции получены', this.all_competences)
      } catch (e) {
        alert('Ошибка получения компетенций');
      }
    },
    showDialog(compenetce) {
      this.dialogVisible = true;
      this.selectedCompetence = compenetce;
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