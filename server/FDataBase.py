import json
from owlready2 import *
from psycopg2 import OperationalError
import MyOntology
import UploadProtegeFile

with open('data.json', encoding='utf-8') as json_file:
    dictionary = json.load(json_file)


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_student(self, user_id):
        pass

    def register_student(self, student):
        insert_user_query = f"INSERT INTO users(login, password, role_id) " \
                            f"VALUES ('{student['login']}', '{student['password']}', 2) " \
                            f"returning user_id;"
        self.__cur.execute(insert_user_query)
        result_user_id = self.__cur.fetchone()
        print('айди пользователя', result_user_id[0])
        self.__db.commit()

        insert_student_query = f"INSERT INTO student(record_book_number, surname, name, patronymic, e_mail, user_id) " \
                               f"VALUES ({student['record_book_number']}, '{student['surname']}', " \
                               f"'{student['name']}', '{student['patronymic']}', " \
                               f"'{student['e_mail']}', {result_user_id[0]});"
        self.__cur.execute(insert_student_query)
        self.__db.commit()

    def check_and_get_user(self, login, password):
        check_user_query = f"SELECT user_id, login, password, role_id " \
                           f"FROM public.users " \
                           f"WHERE login='{login}' " \
                           f"AND password='{password}';"
        self.__cur.execute(check_user_query)
        result = self.__cur.fetchone()
        if result is not None:
            user_data = {
                'user_id': result[0],
                'login': result[1],
                'role_id': result[3],
            }
            if result[3] == 2:
                get_student_query = f"SELECT record_book_number, surname, name, patronymic, e_mail " \
                                    f"FROM student " \
                                    f"JOIN users USING(user_id)" \
                                    f"WHERE user_id = {user_data['user_id']};"
                self.__cur.execute(get_student_query)
                student_query_result = self.__cur.fetchone()
                user_data['record_book_number'] = student_query_result[0]
                user_data['surname'] = student_query_result[1]
                user_data['name'] = student_query_result[2]
                user_data['patronymic'] = student_query_result[3]
                user_data['e_mail'] = student_query_result[4]
            print('Данные пользователя', user_data)
            return user_data
        else:
            return result

    def set_trajectories_to_student(self, trajectories, stud_id):
        del_query = f"DELETE FROM student_trajectories WHERE student_id = {stud_id};"
        self.execute_query(del_query)
        for i in range(0, len(trajectories)):
            set_query = f"INSERT INTO student_trajectories(student_id, trajectory_id) VALUES ({stud_id}, {trajectories[i]});"
            self.execute_query(set_query)

    def execute_query(self, query):  # для неселектовых запросов
        try:
            self.__cur.execute(query)
            self.__db.commit()
            return []
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    def execute_query_select(self, query):  # для селектовых запросов
        try:
            self.__cur.execute(query)
            result = self.__cur.fetchall()
            return result
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    def get_all_disciplines(self):  # получить все дисциплины (без семестров)
        disciplines_query = """SELECT discipline_name
            FROM basic_discipline
            UNION SELECT discipline_name
            FROM elective_discipline;"""
        try:
            result = self.execute_query_select(disciplines_query)
            result_list = []
            for item in result:
                result_list.append(str(item[0]))
            return result_list
        except:
            print('Ошибка чтения из бд')
            return []

    def get_basic_disciplines(self):  # получить все дисциплины (без семестров)
        disciplines_query = """SELECT discipline_code, discipline_name
            FROM basic_discipline;"""
        try:
            result = self.execute_query_select(disciplines_query)
            result_dict = {}
            for item in result:
                result_dict[str(item[0])] = str(item[1])
            return result_dict
        except:
            print('Ошибка чтения из бд')
            return []

    def get_elective_disciplines(self):  # получить все дисциплины (без семестров)
        disciplines_query = """SELECT discipline_code, discipline_name, taught_per_semester, module_name
	        FROM elective_discipline JOIN module_of_disciplines USING(module_code);"""
        try:
            result = self.execute_query_select(disciplines_query)
            result_list = []
            for item in result:
                disc = {
                    'discipline_code': item[0],
                    'discipline_name': item[1],
                    'taught_per_semester': item[2],
                    'module_name': item[3],
                }
                result_list.append(disc)
            return result_list
        except:
            print('Ошибка чтения из бд')
            return []

    def get_all_trajectories(self):  # получить все дисциплины (без семестров)
        trajectories_query = "SELECT trajectory_id, speciality_code, speciality_name " \
                             "FROM trajectory;"
        try:
            result_tr = self.execute_query_select(trajectories_query)
            result_list = []
            all_disc_list = []
            copmetence_list = []
            for tr in result_tr:
                result_ds = self.get_dics_in_trajec(tr[0])  # получаем дисциплины из траектории с номером tr[0]
                for ds in result_ds:
                    result_competence = self.get_comp_in_dics(ds[0])  # получаем компетенции из дисциплины с номером ds[0]
                    for cm in result_competence:
                        result_comp = {
                            'competence_code': cm[0]
                        }
                        copmetence_list.append(result_comp)
                    comp_for_append_list = copmetence_list.copy()
                    result_dist = {
                        'discipline_code': ds[0],
                        'discipline_name': ds[1],
                        'module_name': ds[2],
                        'competences': comp_for_append_list
                    }
                    copmetence_list.clear()

                    all_disc_list.append(result_dist)
                list_for_append = all_disc_list.copy()
                trajec = {
                    'trajectory_id': tr[0],
                    'speciality_code': tr[1],
                    'speciality_name': tr[2],
                    'disciplines': list_for_append
                }
                all_disc_list.clear()
                result_list.append(trajec)
            return result_list
        except:
            print('Ошибка чтения всех траекторий из бд')
            return []

    def get_student_trajectories(self, stud_id):
        trajectories_query = f"SELECT trajectory.trajectory_id, trajectory.speciality_code, trajectory.speciality_name " \
                             f"FROM trajectory JOIN student_trajectories " \
                             f"ON trajectory.trajectory_id = student_trajectories.trajectory_id " \
                             f"JOIN student " \
                             f"ON student_trajectories.student_id = student.record_book_number " \
                             f"WHERE student_id={2345552}"
        try:
            result_tr = self.execute_query_select(trajectories_query)
            result_list = []
            all_disc_list = []
            copmetence_list = []
            for tr in result_tr:
                result_ds = self.get_dics_in_trajec(tr[0])  # получаем дисциплины из траектории с номером tr[0]
                for ds in result_ds:
                    result_competence = self.get_comp_in_dics(ds[0])  # получаем компетенции из дисциплины с номером ds[0]
                    for cm in result_competence:
                        result_comp = {
                            'competence_code': cm[0]
                        }
                        copmetence_list.append(result_comp)
                    result_dist = {
                        'discipline_code': ds[0],
                        'discipline_name': ds[1],

                        'competenses': result_comp
                    }
                    all_disc_list.append(result_dist)
                trajec = {
                    'trajectory_id': tr[0],
                    'speciality_code': tr[1],
                    'speciality_name': tr[2],
                    'disciplines': all_disc_list
                }
                result_list.append(trajec)
            return result_list
        except:
            print('Ошибка чтения траекторий студента из бд')
            return []

    def get_dics_in_trajec(self, disc_num):
        dics_in_trajec_query = f"SELECT discipline_code, discipline_name, module_name " \
                               f"FROM discipline_in_trajectory " \
                               f"JOIN basic_discipline " \
                               f"USING(discipline_code) " \
                               f"JOIN module_of_disciplines " \
                               f"USING(module_code) " \
                               f"UNION " \
                               f"SELECT discipline_code, discipline_name, module_name " \
                               f"FROM discipline_in_trajectory " \
                               f"JOIN elective_discipline " \
                               f"USING(discipline_code) " \
                               f"JOIN module_of_disciplines " \
                               f"USING(module_code) " \
                               f"WHERE trajectory_id = {disc_num};"
        print(dics_in_trajec_query)
        try:
            result = self.execute_query_select(dics_in_trajec_query)
            return result
        except:
            print('Ошибка чтения дисциплин в траектории бд')
            return []

    def get_comp_in_dics(self, dics_code):
        comp_in_dics_query = f"SELECT competence_code, type_name " \
                             f"FROM discipline_forms_competence " \
                             f"JOIN competence USING(competence_code) " \
                             f"JOIN competence_type USING(type_id) " \
                             f"WHERE discipline_code='{dics_code}';"
        try:
            result = self.execute_query_select(comp_in_dics_query)
            return result
        except:
            print('Ошибка чтения компетенций в дисциплине')
            return []

    def get_all_students(self):  # получить всех студентов
        query = """SELECT surname, name, patronymic, record_book_number, e_mail, login, user_id 
	FROM users JOIN student USING (user_id);"""
        try:
            result_arr = self.execute_query_select(query)
            print(result_arr[0][0])
            result = []
            for item in result_arr:
                result.append({
                    'surname': item[0],
                    'name': item[1],
                    'patronymic': item[2],
                    'record_book_number': item[3],
                    'e_mail': item[4],
                    'login': item[5],
                    'user_id': item[6],
                })
            return result
        except:
            print('Ошибка чтения из бд')
            return []

    def get_all_disciplines_with_semester(self):
        disciplines_query = """SELECT discipline_name, taught_per_semester
            FROM basic_discipline
            UNION SELECT discipline_name, taught_per_semester
            FROM elective_discipline
            ORDER by taught_per_semester;"""
        disciplines_result = self.execute_query_select(disciplines_query)
        return disciplines_result

    def get_trajectory(self, chosen_discipline, user_id, record_book_number, f_name):
        stud = MyOntology.Student('Student_' + str(user_id), None,
                                  full_name=[f_name],
                                  record_book_number=[record_book_number])
        stud.label = locstr('Студент ' + str(user_id), lang="ru")
        owlready2.sync_reasoner_pellet()  # запуск решателя

        for choos_disc in chosen_discipline:
            # query = f"INSERT INTO selected_disciplines(student_id, discipline_code) " \
            # f"VALUES ({rec_book_num}, {});"
            for item in MyOntology.Elective_discipline.instances():
                if item.name == MyOntology.get_key(dictionary,
                                                   choos_disc):  # сравниваем поочерёдно все предметы из списка с введённым
                    stud.chooses.append(item)  # добавляем предметы которые выбирает

            for item in MyOntology.Basic_discipline.instances():
                if item.name == MyOntology.get_key(dictionary,
                                                   choos_disc):  # сравниваем поочерёдно все предметы из списка с введённым
                    stud.chooses.append(item)  # добавляем предметы которые выбирает

        owlready2.sync_reasoner_pellet(infer_property_values=True,
                                       infer_data_property_values=True)  # запуск решателя чтоб достать траекторию
        result_trajectory = []

        for stud_trajec in stud.builds:  # траектории
            result_trajectory.append(stud_trajec.name)

        MyOntology.onto.save('test_onto_for_db_for_change.owl')  # куда сохранить онтологию
        destroy_entity(stud)  # удаляем сущность студента
        return result_trajectory
