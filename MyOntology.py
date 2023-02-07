from owlready2 import *

# =================================ЗАГРУЖАЕМ ОНТОЛОГИЮ======================
onto_path.append("D:/work/diploma")
onto = get_ontology("file:///work/7_sem/diploma/test_onto_for_db.owl")
onto.load()

with onto:
    # =================================Classes==============================
    class Student(Thing):
        pass


    class Discipline(Thing):
        pass


    class Basic_discipline(Discipline):
        pass


    class Elective_discipline(Discipline):
        pass


    class Competence(Thing):
        pass


    class General_professional_competence(Competence):
        pass


    class Professional_competence(Competence):
        pass


    class Universal_competence(Competence):
        pass


    class Speciality(Thing):
        pass


    class Trajectory(Thing):
        pass


    # =================================EndClasses==============================

    # ================================ObjectProperty===========================
    class leads(ObjectProperty):  # ведёт
        domain = [Trajectory]
        range = [Speciality]


    class chooses(ObjectProperty):  # выбирает
        domain = [Student]
        range = [Discipline]


    class acquired_by_studying(ObjectProperty):  # приобретается при изучении
        domain = [Competence]


    class develops(ObjectProperty):  # вырабатывает
        domain = [Discipline]
        range = [Competence]
        inverse_property = acquired_by_studying


    class acquires(ObjectProperty):  # приобретает
        domain = [Student]
        range = [Competence]


    class contains(ObjectProperty):  # содержит
        domain = [Trajectory]
        range = [Discipline]


    class seeks(ObjectProperty):  # стремится
        domain = [Student]
        range = [Speciality]


    class builds(ObjectProperty):  # строит
        domain = [Student]
        range = [Trajectory]


    class forms(ObjectProperty):  # формирует
        domain = [Competence]
        range = [Speciality]


    # =============================EndObjectProperty=========================

    # ================================DataProperty===========================
    class has_code(DataProperty):  # имеет код
        domain = [Speciality]
        range = [str]


    class record_book_number(DataProperty):  # номер зачётной книжки
        domain = [Student]
        range = [int]


    class refers_to(DataProperty):  # относится к
        domain = [Competence]
        range = [str]


    class taught_per_semester(DataProperty):  # преподаётся в семестре
        domain = [Discipline]
        range = [int]


    class full_name(DataProperty):  # ФИО
        domain = [Student]
        range = [str]


    class is_a_obj(DataProperty):  # является
        domain = [Discipline]
        range = [str]


    def get_key(dct, value):
        for k, v in dct.items():
            if v == value:
                return k

