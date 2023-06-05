<template>
  <div class="container-wrapper container">
    <section class="content col-lg-8 mx-auto">
      <div class="settings-elem">
        <email-change-form></email-change-form>
        <password-change-form></password-change-form>
      </div>


    </section>
  </div>
</template>

<script>
import EmailChangeForm from "@/components/EmailChangeForm";
import PasswordChangeForm from "@/components/PasswordChangeForm";
export default {
  name: "settings-page",
  components: {PasswordChangeForm, EmailChangeForm}
}
</script>

<style scoped>
.settings-elem{
  margin-top: 100px;
}
</style>