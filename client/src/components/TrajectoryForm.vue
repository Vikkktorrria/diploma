<template>
    <div class="login_form_elem col-10 mx-auto">
      <form>
        <div class="accordion" id="accordionPanelsStayOpenExample">


          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-heading1">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse1" aria-expanded="false" aria-controls="panelsStayOpen-collapse1">
                Траектория 1 (Программист)
              </button>
            </h2>
            <div id="panelsStayOpen-collapse1" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading1">
              <div class="accordion-body">
                Программирование<br>
                Базы данных<br>
                Управление базами данных<br>
                Инженерия программного обеспечения<br>
                Объектно-ориентированное программирование<br>
                Структуры и алгоритмы обработки данных<br>
                Информатика<br>
                Системное программирование<br>

              </div>
            </div>
          </div>

          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-heading2">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse2" aria-expanded="false" aria-controls="panelsStayOpen-collapse2">
                Траектория 2 (Технический писатель)
              </button>
            </h2>
            <div id="panelsStayOpen-collapse2" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading2">
              <div class="accordion-body">
                Программирование<br>
                Базы данных<br>
                Управление базами данных<br>
                Инженерия программного обеспечения<br>
                Объектно-ориентированное программирование<br>
                Структуры и алгоритмы обработки данных<br>
                Информатика<br>
                Системное программирование<br>

              </div>
            </div>
          </div>

          <div class="accordion-item">
            <h2 class="accordion-header" id="panelsStayOpen-heading3">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse3" aria-expanded="false" aria-controls="panelsStayOpen-collapse3">
                Траектория 3 (Администратор баз данных)
              </button>
            </h2>
            <div id="panelsStayOpen-collapse3" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading3">
              <div class="accordion-body">
                Программирование<br>
                Базы данных<br>
                Управление базами данных<br>
                Инженерия программного обеспечения<br>
                Объектно-ориентированное программирование<br>
                Структуры и алгоритмы обработки данных<br>
                Информатика<br>
                Системное программирование<br>

              </div>
            </div>
          </div>




        </div>
      </form>
    </div>
</template>

<script>
export default {
  name: "trajectory-form"
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
</style>