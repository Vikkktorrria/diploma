<template>

  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">

      <registration-form/>

      <footer class="footer row">

      </footer>

    </section>


  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm";
export default {
  name: "student-registration",
  components: {RegistrationForm},
}
</script>

<style scoped>

</style>