<template>
  <div class="change_data_table">
    <h2>Редактирование траектории</h2>
    <p><strong>Номер траектории:</strong><input :value="this.trajectory.trajectory_id"></p>
    <p><strong>Код специальности:</strong><input :value="this.trajectory.speciality_code"></p>
    <p><strong>Название специальности:</strong><input :value="this.trajectory.speciality_name"></p>
    <details>
      <summary><label>Дисциплины</label></summary>
      <div class="disciplines_list"
          v-for="dics in trajectory.disciplines"
          :key="dics.discipline_code"
      ><p>{{ dics.discipline_name}}</p></div>
    </details>

  </div>
  <button>Сохранить</button>
</template>

<script>
export default {
  name: "trajectory-table",
  props: {
    trajectory: {
      type: Object,
      required: true,
    },
  },
  mounted(){
    console.log(this.trajectory)
  },
}

</script>

<style scoped>
.modal {
  /* Стили для модального окна */
}

.modal-content {
  /* Стили для содержимого модального окна */
}

.close {
  /* Стили для кнопки закрытия модального окна */
}
</style>