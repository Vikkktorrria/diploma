<template>
    <div class="login_form_elem col-10 mx-auto">
      <form>

        <div v-if="stud_trajectories !== null"
            class="accordion" id="accordionPanelsStayOpenExample">
          <strong><p class="trajec_header">Траектории студента</p></strong>
          <div
              v-for="trajec in stud_trajectories"
              :key="trajec.trajectory_id"
              class="accordion-item"
          >
            <h2
                class="accordion-header"
                :id="'panelsStayOpen-heading' + trajec.trajectory_id + 1">

              <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  :data-bs-target="'#panelsStayOpen-collapse' + trajec.trajectory_id + 1"
                  aria-expanded="false"
                  :aria-controls="'panelsStayOpen-collapse' + trajec.trajectory_id + 1">
                <span>Траектория {{trajec.trajectory_id}} ({{trajec.speciality_code}} - {{trajec.speciality_name}})</span>

              </button>
            </h2>
            <div
                :id="'panelsStayOpen-collapse' + trajec.trajectory_id + 1"
                class="accordion-collapse collapse"
                :aria-labelledby="'panelsStayOpen-heading' + trajec.trajectory_id + 1">
              <div class="accordion-body">
                <ul id="array-rendering"
                    v-for="disc in trajec.disciplines"
                    :key="disc.discipline_code"
                >
                  <li>
                    <div :id="disc.discipline_code" :value="disc.discipline_name"></div>
                    <details>
                      <summary><label>{{disc.discipline_name}}</label></summary>
                      <div
                          v-for="comp in disc.competences"
                          :key="comp.competence_code"
                      ><p class="accordion_details">{{comp.competence_code}}</p></div>
                    </details>
                  </li>
                </ul>
              </div>
            </div>
          </div>



        </div>










        <div class="accordion" id="accordionPanelsStayOpenExample">
          <strong><p class="trajec_header">Все траектории</p></strong>
        <div
            v-for="trajec in all_trajectories"
            :key="trajec.trajectory_id"
            class="accordion-item"
        >
          <h2
              class="accordion-header"
              :id="'panelsStayOpen-heading' + trajec.trajectory_id">

            <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                :data-bs-target="'#panelsStayOpen-collapse' + trajec.trajectory_id"
                aria-expanded="false"
                :aria-controls="'panelsStayOpen-collapse' + trajec.trajectory_id">
              <span>Траектория {{trajec.trajectory_id}} ({{trajec.speciality_code}} - {{trajec.speciality_name}})</span>

            </button>
          </h2>
          <div
              :id="'panelsStayOpen-collapse' + trajec.trajectory_id"
              class="accordion-collapse collapse"
              :aria-labelledby="'panelsStayOpen-heading' + trajec.trajectory_id">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="disc in trajec.disciplines"
                  :key="disc.discipline_code"
              >
                <li>
                  <div :id="disc.discipline_code" :value="disc.discipline_name"></div>
                  <details>
                    <summary><label>{{disc.discipline_name}}</label></summary>
                    <div
                        v-for="comp in disc.competences"
                        :key="comp.competence_code"
                    ><p class="accordion_details">{{comp.competence_code}}</p></div>
                  </details>
                </li>
              </ul>
            </div>
          </div>
        </div>
        </div>







      </form>
    </div>
</template>

<script>

export default {

  name: "trajectory-form",
  props:{
    all_trajectories:{
      type: Array,
    },
    stud_trajectories:{
      type: Array,
    },

  },

}
</script>

<style scoped>
.accordion{
  text-align: left;
  margin-top: 50px;
}
.accordion-item{
}
li{
  list-style-type: none;
}
.change_data_symbol{
  color: red;
}
summary{
  font-size: 16px;
}
.trajec_header{
  text-align: center;
  font-size: 20px;
}
.accordion_details{
  color: #656565;
}
</style>