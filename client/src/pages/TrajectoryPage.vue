<template>
    <div class="container-wrapper container">
      <section class="content col-lg-8 mx-auto">
        <trajectory-form v-if="this.user.role_id === 2"
            v-bind:all_trajectories="all_trajectories"
            v-bind:stud_trajectories="stud_trajectories.length > 0 ? stud_trajectories : null"
        />



        <div v-if="this.user.role_id === 1"
        >
          <table>
            <thead>
            <tr class="header_row">
              <th>Номер траектории</th>
              <th>Код специальности</th>
              <th>Название специальности</th>
              <th>Дисциплины</th>
            </tr>
            </thead>
            <tbody>
            <tr class="content_row"
                v-for="trajec in all_trajectories"
                :key="trajec.trajectory_id"
                @dblclick="showDialog(trajec)">
              <td>{{ trajec.trajectory_id }}</td>
              <td>{{ trajec.speciality_code }}</td>
              <td>{{ trajec.speciality_name }}</td>

              <td>
                <details>
                  <summary><label></label></summary>
                  <ul>
                      <div
                        v-for="dics in trajec.disciplines"
                        :key="dics.discipline_code"
                    >
                        <li class="disciplines_list"><p>{{ dics.discipline_name}}</p></li>
                      </div>
                  </ul>


              </details>
              </td>
            </tr>
            </tbody>
          </table>
        </div>

        <modal-window v-model:show="dialogVisible">
          <trajectory-table :trajectory="selectedTrajectory"/>
        </modal-window>



      </section>


    </div>
</template>

<script>
import TrajectoryForm from "@/components/TrajectoryForm";
import axios from "axios";
import {mapGetters} from "vuex";
import TrajectoryTable from "@/components/Tables/TrajectoryTable";
import ModalWindow from "@/components/ModalWindow";

export default {
  computed:{
    ...mapGetters(['getUser']),
    user(){
      return this.$store.getters.getUser; // Получение данных пользователя из геттера
    }
  },
  data(){
    return{
      all_trajectories: [],
      stud_trajectories: [],
      dialogVisible: false,
      selectedTrajectory: null,
    }
  },
  name: "trajectories-page",
  components: {TrajectoryTable, TrajectoryForm, ModalWindow},
  methods:{
    async fetchAllTrajectories() { // функция для получения данных с сервера
      try{
        const response = await axios.get('trajectory/all');
        this.all_trajectories = response.data;
      } catch(e){
        alert('Ошибка получения траекторий');
      }
    },
    async fetchStudentTrajectories(student_id) { // функция для получения данных с сервера
      try{
        const response = await axios.get('trajectory/my', {
          params: {
            student_id: student_id
          }
        });
        this.stud_trajectories = response.data;
        console.log(this.all_trajectories)
        console.log(this.stud_trajectories)
        if (this.stud_trajectories.length == 0){
          this.stud_trajectories = 'Построенных траекторий пока нет';
        }
      } catch(e){
        alert('Ошибка получения дисциплин');
      }
    },
    showDialog(trajectory) {
      console.log('вонючее модальное окно откройся')
      this.dialogVisible = true;
      this.selectedTrajectory = trajectory;
    }
  },
  mounted(){
    this.fetchAllTrajectories();
    if (this.user.role_id === 2){
      this.fetchStudentTrajectories(this.user.record_book_number);
    }
    console.log('дисциплины получаются');
  },
}
</script>

<style scoped>
.disciplines_list{
  text-align: left;
}
.content_row{
  vertical-align: top;
}
</style>