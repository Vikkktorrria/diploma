<template>
  <div class="login_form_elem col-10 mx-auto">
    <form @submit.prevent>

      <div class="accordion" id="accordionPanelsStayOpenExample">
        <strong><p class="disc_header">Выберите интересующие Вас дисциплины</p></strong>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading1">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse1" aria-expanded="false" aria-controls="panelsStayOpen-collapse1">
              Общие дисциплины
            </button>
          </h2>
          <div id="panelsStayOpen-collapse1" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading1">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Общие'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>



        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading2">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse2" aria-expanded="false" aria-controls="panelsStayOpen-collapse2">
              Системное администрирования
              автоматизированных систем управления
            </button>
          </h2>
          <div id="panelsStayOpen-collapse2" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading2">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Системное администрирования автоматизированных систем управления'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
          </div>
        </div>
          </div>


        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading3">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse3" aria-expanded="false" aria-controls="panelsStayOpen-collapse3">
              Хранение и обработка данных в автоматизированных системах управления
            </button>
          </h2>
          <div id="panelsStayOpen-collapse3" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading3">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Хранение и обработка данных в автоматизированных системах управления'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>


        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading4">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse4" aria-expanded="false" aria-controls="panelsStayOpen-collapse4">
              Внедрение и сопровождение автоматизированных систем управления
            </button>
          </h2>
          <div id="panelsStayOpen-collapse4" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading4">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Внедрение и сопровождение автоматизированных систем управления'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>


        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading5">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse5" aria-expanded="false" aria-controls="panelsStayOpen-collapse5">
              Элективные дисциплины по физической культуре и спорту
            </button>
          </h2>
          <div id="panelsStayOpen-collapse5" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading5">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Элективные дисциплины по физической культуре и спорту'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>


        <div class="accordion-item">
          <h2
              class="accordion-header"
              id="panelsStayOpen-heading6">
            <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-collapse6"
                aria-expanded="false"
                aria-controls="panelsStayOpen-collapse6">
              Элективные дисциплины 1
            </button>
          </h2>
          <div
              id="panelsStayOpen-collapse6"
              class="accordion-collapse collapse"
              aria-labelledby="panelsStayOpen-heading6">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Элективные дисциплины 1'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>


        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading7">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse7" aria-expanded="false" aria-controls="panelsStayOpen-collapse7">
              Элективные дисциплины 2
            </button>
          </h2>
          <div id="panelsStayOpen-collapse7" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading7">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Элективные дисциплины 2'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>


        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-heading8">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse8" aria-expanded="false" aria-controls="panelsStayOpen-collapse8">
              Элективные дисциплины 3
            </button>
          </h2>
          <div id="panelsStayOpen-collapse8" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading8">
            <div class="accordion-body">
              <ul id="array-rendering"
                  v-for="item in elective_disciplines"
                  :key="item.discipline_code"
              >
                <li  v-if="item.module_name === 'Элективные дисциплины 3'"
                >
                  <input type="checkbox" :id="item.discipline_code" :value="item.discipline_name" v-model="checkedDisciplines">
                  <label>{{item.discipline_name}}</label>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <button class="btn"
            type="submit"
            @click="submitDisciplines"
        >
          Сохранить
        </button>
        <button class="btn">Сбросить выбор</button>

      </div>
    </form>
  </div>


</template>

<script>
import axios from "axios";
import { getUser } from '@/store/authModule'
import {mapGetters} from "vuex";

export default {
  computed:{
    ...mapGetters(['getUser']),
    user(){
      return getUser()
    }
  },
  props:{
    elective_disciplines:{
      type: Array,
    }
  },
  data() {
    return {
      checkedDisciplines: [],
      data_for_submit: {},
    }
  },
  methods: {
    async submitDisciplines() { // функция для отправления данных на сервер
      try{

        const user = this.getUser // текущий авторизованный пользователь
        this.data_for_submit = {
          'disciplines': this.checkedDisciplines, // выбранные дисциплины
          'student': user,
        }
        console.log('данные для отправки', this.data_for_submit)
        await axios.post('disciplines', this.data_for_submit);
        // передаём дисциплины и пользователя
        this.$router.push({
          name: 'trajectory',
        })
      } catch(e){
        alert('Ошибка отправки дисциплин');
      }
    },
  },
  name: "disciplines-form",

}

</script>

<style scoped>
.accordion{
  text-align: left;
  margin-top: 50px;
}
.accordion-item{
}
button{
  text-align: center;
}
li{
  list-style-type: none;
}
label{
  margin-left: 10px;
}
.disc_header{
  text-align: center;
  font-size: 20px;
}
</style>