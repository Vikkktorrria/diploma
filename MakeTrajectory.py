from owlready2 import *
import Connection as cn
import json
import MyOntology
import UploadProtegeFile


with open('data.json', encoding='utf-8') as json_file:
    dictionary = json.load(json_file)


def get_all_disciplines():  # получить все дисциплины (без семестров)
    disciplines_query = """SELECT discipline_name
    	FROM basic_discipline
        UNION SELECT discipline_name
    	FROM elective_discipline;"""
    disciplines_result = list(cn.execute_query_SELECT(disciplines_query))
    result_list = []
    for item in disciplines_result:
        result_list.append(str(item[0]))
    print(disciplines_result)
    print(result_list)
    return result_list


def get_all_disciplines_with_semester():
    disciplines_query = """SELECT discipline_name, taught_per_semester
    	FROM basic_discipline
        UNION SELECT discipline_name, taught_per_semester
    	FROM elective_discipline
        ORDER by taught_per_semester;"""
    disciplines_result = cn.execute_query_SELECT(disciplines_query)
    return disciplines_result


def get_trajectory(chosen_discipline):
    print(chosen_discipline)

    stud = MyOntology.Student('Student_2', None,
                            full_name=['Копыльских Виктория Максимовна'],
                            record_book_number=[2345552])
    stud.label = locstr('Студент 2', lang="ru")
    sync_reasoner_pellet()  # запуск решателя

    for choos_disc in chosen_discipline:
        for item in MyOntology.Elective_discipline.instances():
            if item.name == MyOntology.get_key(dictionary,
                                             choos_disc):  # сравниваем поочерёдно все предметы из списка с введённым
                stud.chooses.append(item)  # добавляем предметы которые выбирает
                print(item)

        for item in MyOntology.Basic_discipline.instances():
            if item.name == MyOntology.get_key(dictionary,
                                             choos_disc):  # сравниваем поочерёдно все предметы из списка с введённым
                stud.chooses.append(item)  # добавляем предметы которые выбирает
                print(item)

    sync_reasoner_pellet(infer_property_values=True,
                         infer_data_property_values=True)  # запуск решателя чтоб достать траекторию
    trajectory_disc = {}
    cont_disc_list = []
    for stud_trajec in stud.builds:
        cont_disc_list.clear()
        for disc in stud_trajec.contains:
            cont_disc_list.append(str(disc.label[0]))
        trajectory_disc[str(stud_trajec.label[0])] = cont_disc_list  # траектория и предметы в траектории
    print(trajectory_disc)
    for item in trajectory_disc:
        print(item, trajectory_disc[item])

    MyOntology.onto.save('test_onto_for_db_for_change.owl')  # куда сохранить онтологию
    return trajectory_disc
