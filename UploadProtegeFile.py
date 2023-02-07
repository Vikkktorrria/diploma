from owlready2 import *
import Connection as cn
import json
import MyOntology

# =================================подключаемся к бд==============================




# =================================ЗАГРУЖАЕМ JSON============================
with open('data.json', encoding='utf-8') as json_file:
    dictionary = json.load(json_file)

basic_disc_develops_comp_query = 'SELECT discipline_name, competence_code' \
                                 ' FROM basic_discipline JOIN discipline_forms_competence USING(discipline_code);'
basic_disc_develops_comp_result = cn.execute_query_SELECT(basic_disc_develops_comp_query)  # дисциплины вырабатывают компетенции

competence_type_query = 'SELECT competence_code, type_name ' \
                        'FROM competence_type ' \
                        'JOIN competence USING(type_id);'
competence_type_result = cn.execute_query_SELECT(competence_type_query)  # тип компетенции

basic_disc_query = 'SELECT discipline_code, discipline_name, taught_per_semester' \
                   ' FROM basic_discipline;'
basic_disc_result = cn.execute_query_SELECT(basic_disc_query)

for item in basic_disc_result:

    eng_title = MyOntology.get_key(dictionary, item[1])
    rus_title = item[1]
    semester = item[2]
    dis = MyOntology.Discipline(eng_title, None,
                                taught_per_semester=[semester],
                                is_a_obj=["basic"],
                                develops=[],
                                refers_to=[])
    dis.label = locstr(rus_title, lang="ru")  # переводим на русский аннотацию

    for item2 in basic_disc_develops_comp_result:
        disc_name = item2[0]
        comp_name = item2[1]
        if dis.name == MyOntology.get_key(dictionary, disc_name):
            # print(dis.name, ontology.get_key(dictionary, disc_name))
            cmptnc = MyOntology.Competence(MyOntology.get_key(dictionary, comp_name), None)
            cmptnc.label = locstr(comp_name, lang="ru")
            for comp_type in competence_type_result:
                if cmptnc.name == MyOntology.get_key(dictionary, comp_type[0]):
                    cmptnc.refers_to.append(MyOntology.get_key(dictionary, comp_type[1]))

            dis.develops.append(cmptnc)  # дисциплина вырабатывает компетенцию
            # cmptnc.acquired_by_studying.append(dis)  # компетенция приобретается при изучении

elective_disc_query = """SELECT discipline_code, 
                                discipline_name, 
                                taught_per_semester
                         FROM elective_discipline;"""
elective_disc_result = cn.execute_query_SELECT(elective_disc_query)

elective_disc_develops_comp_query = 'SELECT discipline_name, competence_code' \
                                    ' FROM elective_discipline JOIN discipline_forms_competence USING(discipline_code);'
elective_disc_develops_comp_result = cn.execute_query_SELECT(elective_disc_develops_comp_query)  # дисциплины вырабатывают компетенции

for item in elective_disc_result:
    eng_title = MyOntology.get_key(dictionary, item[1])
    rus_title = item[1]
    semester = item[2]
    dis = MyOntology.Discipline(eng_title, None,
                                taught_per_semester=[semester],
                                is_a_obj=["elective"])
    dis.label = locstr(rus_title, lang="ru")  # переводим на русский аннотацию

    for item2 in elective_disc_develops_comp_result:
        disc_name = item2[0]
        comp_name = item2[1]
        if dis.name == MyOntology.get_key(dictionary, disc_name):
            # print(dis.name, ontology.get_key(dictionary, disc_name))
            cmptnc = MyOntology.Competence(MyOntology.get_key(dictionary, comp_name), None)
            cmptnc.label = locstr(comp_name, lang="ru")
            for comp_type in competence_type_result:
                if cmptnc.name == MyOntology.get_key(dictionary, comp_type[0]):
                    cmptnc.refers_to.append(MyOntology.get_key(dictionary, comp_type[1]))

            dis.develops.append(cmptnc)  # дисциплина вырабатывает компетенцию
            # cmptnc.acquired_by_studying.append(dis)  # компетенция приобретается при изучении
            # print(dis.name, cmptnc.name)

comp_forms_trajectory_query = 'SELECT DISTINCT competence_code, speciality_code, speciality_name, trajectory_id ' \
                              'FROM discipline_forms_competence ' \
                              'JOIN discipline_in_trajectory USING(discipline_code) ' \
                              'JOIN trajectory USING(trajectory_id)' \
                              'ORDER BY competence_code;'
comp_forms_trajectory_result = cn.execute_query_SELECT(comp_forms_trajectory_query)  # компетенции формируют спефиальность

trajectory_query = """SELECT trajectory_id, speciality_code, speciality_name
	                            FROM trajectory;"""
trajectory_result = cn.execute_query_SELECT(trajectory_query)  # траектории

elective_disc_in_tr_query = """SELECT discipline_name, trajectory_id
	                        FROM discipline_in_trajectory
                            JOIN elective_discipline using(discipline_code);"""
elective_disc_in_tr_result = cn.execute_query_SELECT(elective_disc_in_tr_query)  # дисциплины в траекториях

basic_disc_in_tr_query = """SELECT discipline_name, trajectory_id
	                        FROM discipline_in_trajectory
                            JOIN basic_discipline using(discipline_code);"""
basic_disc_in_tr_result = cn.execute_query_SELECT(basic_disc_in_tr_query)  # дисциплины в траекториях

for trj in trajectory_result:
    trajec_id = trj[0]
    spec_code = trj[1]
    spec_name = trj[2]
    trajec_name = 'Trajectory_' + str(trajec_id)

    special = MyOntology.Speciality(MyOntology.get_key(dictionary, spec_name), None, has_code=[spec_code])
    traject = MyOntology.Trajectory(trajec_name, None, leads=[special])
    special.label = locstr(spec_name, lang="ru")
    traject.label = locstr('Траектория ' + str(trajec_id), lang="ru")

    for item in comp_forms_trajectory_result:
        comp_code = item[0]
        spec_code2 = item[1]
        spec_name2 = item[2]

        if spec_name == spec_name2:
            for i in MyOntology.Competence.instances():
                if i.name == MyOntology.get_key(dictionary, comp_code):
                    i.forms.append(special)

for trj in MyOntology.Trajectory.instances():
    # =======================ДОБАВЛЯЮ ЭЛЕКТИВНЫЕ ДИСЦИПЛИНЫ В ТРАЕКТОРИИ===========================
    for item in elective_disc_in_tr_result:
        disc_name = item[0]
        tr_id = item[1]
        if trj.name == 'Trajectory_' + str(tr_id):
            for ds in MyOntology.Discipline.instances():
                if ds.name == MyOntology.get_key(dictionary, disc_name):
                    trj.contains.append(ds)

    # =======================ДОБАВЛЯЮ БАЗОВЫЕ ДИСЦИПЛИНЫ В ТРАЕКТОРИИ===========================
    for item in basic_disc_in_tr_result:
        disc_name = item[0]
        tr_id = item[1]
        if trj.name == 'Trajectory_' + str(tr_id):
            for ds in MyOntology.Discipline.instances():
                if ds.name == MyOntology.get_key(dictionary, disc_name):
                    trj.contains.append(ds)
    # ========================================================================================





# sync_reasoner_pellet()  # запуск решателя

# sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)  # запуск решателя чтоб достать траекторию


MyOntology.onto.save('test_onto_for_db_for_change.owl')  # куда сохранить онтологию
