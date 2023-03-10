<template>
  <div class="profile_item row-cols-1">
    <user-card/>
    <user-num/>
    <user-e-mail/>
  </div>
</template>

<script>
import UserCard from "@/components/Profile/UserCard";
import UserNum from "@/components/Profile/UserNum";
import UserEMail from "@/components/Profile/UserEMail";
export default {
  props:{
    current_user:{
      type: Object,
    }
  },
  name: "user-form",
  components: {UserEMail, UserNum, UserCard}
}
</script>

<style scoped>

</style>