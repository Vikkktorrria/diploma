<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">

      <registration-form
          @registr="studentRegistration"
      >
      </registration-form>


    </section>


  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm";
import axios from "axios";
export default {
  name: "student-registration",
  components: {RegistrationForm},
  data() {
    return {
      student: {
        surname: '',
        name: '',
        patronymic: '',
        record_book_number: '',
        e_mail: '',
        login: '',
        password: '',
      },
    }
  },
  methods: {
    async studentRegistration(student){
      this.student = student;
      console.log('студент', this.student)
      try {
        console.log('студент зарегистрирован', this.student)
        await axios.post('/student/registration', this.student)


      } catch (error) {
        if (error.response.status === 401) {
          console.log('Неверный логин или парольиус')
        }
      }
    }
  }
}
</script>

<style scoped>

</style>