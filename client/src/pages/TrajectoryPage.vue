<template>
    <div class="container-wrapper container">
      <section class="content col-lg-8 mx-auto">
        <trajectory-form
            v-bind:all_trajectories="all_trajectories"
        />
        <footer class="footer row">

        </footer>

      </section>


    </div>
</template>

<script>
import TrajectoryForm from "@/components/TrajectoryForm";
import axios from "axios";
export default {
  data(){
    return{
      all_trajectories: [],
      stud_trajectories: [],
    }
  },
  name: "trajectories-page",
  components: {TrajectoryForm},
  methods:{
    async fetchAllTrajectories() { // функция для получения данных с сервера
      try{
        const response = await axios.get('trajectory/all');
        this.all_trajectories = response.data;
      } catch(e){
        alert('Ошибка получения дисциплин');
      }
    },
  },
  mounted(){
    this.fetchAllTrajectories();
    console.log('дисциплины получаются');
  },
}
</script>