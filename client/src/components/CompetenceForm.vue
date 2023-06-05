<template>
  <div class="login_form_elem col-10 mx-auto">
    <form>
      <div class="accordion" id="accordionPanelsStayOpenExample">
        <strong><p class="comp_header">Компетенции и их описание</p></strong>
        <div
            v-for="competence in all_competences"
            :key="competence.competence_code"
            class="accordion-item"
        >
          <h2
              class="accordion-header"
              :id="'panelsStayOpen-heading' + competence.competence_code">

            <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                :data-bs-target="'#panelsStayOpen-collapse' + competence.competence_code"
                aria-expanded="false"
                :aria-controls="'panelsStayOpen-collapse' + competence.competence_code">
              <span>{{competence.competence_code}} ({{competence.type_name}})</span>

            </button>



          </h2>
          <div
              :id="'panelsStayOpen-collapse' + competence.competence_code"
              class="accordion-collapse collapse"
              :aria-labelledby="'panelsStayOpen-heading' + competence.competence_code">
            <div class="accordion-body">
              {{competence.description}}
            </div>
          </div>

        </div>





      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "CompetenceForm",
  props:{
    all_competences:{
      type: Array,
    },
  },
  mounted(){
    console.log('описание', this.all_competences.description);
  },
}
</script>

<style scoped>
.accordion-body{
  text-align: left;
  color: #656565;
}
.accordion{
  margin-top: 50px;
}
.comp_header{
  text-align: center;
  font-size: 20px;
}
</style>