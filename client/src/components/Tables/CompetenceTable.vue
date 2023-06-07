<template>
  <div class="change_data_modal_table">
    <div class="change_data_header_table">Редактирование компетенции</div>
    <p class="table_item"><strong>Код компетенции:</strong><input :value="this.compenetce.competence_code" class="table_data_input disabled" disabled></p>
    <p class="table_item"><strong>Тип компетенции:</strong><input :value="this.compenetce.type_name" class="table_data_input disabled" disabled></p>
    <p class="table_item"><strong>Описание:</strong><textarea class="table_data_input" v-model="description"></textarea></p>
  </div>
  <button class="btn">Сохранить</button>
</template>

<script>
export default {
  name: "competence-table",
  props: {
    compenetce: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      description: this.compenetce.description
    };
  },
}
</script>

<style scoped>
textarea{
  min-height: 250px;
  min-width: 400px;
  border: none;
  border-bottom: 2px solid #f0f0f0;
  padding-left: 10px;
  color: #35538d;
  font-size: 18px;
  resize: none;
  margin-left: 10px;
}
strong{
  vertical-align: top;
}
</style>