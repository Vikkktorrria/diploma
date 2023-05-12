import json
from owlready2 import *
from psycopg2 import OperationalError
import MyOntology
from flask_login import current_user
from flask import jsonify

with open('data.json', encoding='utf-8') as json_file:
    dictionary = json.load(json_file)


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_student(self, user_id):
       pass

    def check_and_get_user(self, login, password):
        check_user_query = f"SELECT user_id, login, password, role_id " \
                           f"FROM public.users " \
                           f"WHERE login='{login}' " \
                           f"AND password='{password}';"
        self.__cur.execute(check_user_query)
        result = self.__cur.fetchone()
        if result is not None:
            disc_user_data = {
                'user_id': result[0],
                'login': result[1],
                'role_id': result[3],
            }
            return disc_user_data
        else:
            return result





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


    def get_all_students(self):  # получить всех студентов
        query = """SELECT full_name, record_book_number, e_mail, login, user_id 
	FROM users JOIN student USING (user_id);"""
        try:
            result_arr = self.execute_query_select(query)
            print(result_arr[0][0])
            result = []
            for item in result_arr:
                result.append({
                    'full_name': item[0],
                    'record_book_number': item[1],
                    'e_mail': item[2],
                    'login': item[3],
                    'user_id': item[4],
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


    def get_trajectory(self, chosen_discipline):
        #st_num = current_user.get_id()
        #rec_book_num = int(current_user.get_record_book_number())
        #f_name = current_user.get_name()
        st_num = 2
        rec_book_num = 434343
        f_name = 'Victoria'

        stud = MyOntology.Student('Student_' + str(st_num), None,
                                  full_name=[f_name],
                                  record_book_number=[rec_book_num])
        stud.label = locstr('Студент ' + str(st_num), lang="ru")
        owlready2.sync_reasoner_pellet()  # запуск решателя

        for choos_disc in chosen_discipline:
            #query = f"INSERT INTO selected_disciplines(student_id, discipline_code) " \
                    #f"VALUES ({rec_book_num}, {});"
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
        trajectory_disc = {}
        trajectory_list_for_db = []
        cont_disc_list = []
        for stud_trajec in stud.builds:  # траектории
            cont_disc_list.clear()
            for disc in stud_trajec.contains:  # дисциплины
                cont_disc_list.append(str(disc.label[0]))
            trajectory_disc[str(stud_trajec.label[0])] = cont_disc_list # траектория и предметы в траектории (было str(stud_trajec.label[0])
            trajectory_list_for_db.append(stud_trajec.name)


        #delete_query = f"DELETE FROM student_trajectories WHERE student_id = {current_user.get_record_book_number()}"
        #self.execute_query(delete_query)

        #print(trajectory_list_for_db)
        #for tr in trajectory_list_for_db:
            #query_for_insert_trajectory = f"INSERT INTO student_trajectories(student_id, trajectory_id) " \
                                          #f"VALUES ({current_user.get_record_book_number()}, {tr})"
            #self.execute_query(query_for_insert_trajectory)

        MyOntology.onto.save('test_onto_for_db_for_change.owl')  # куда сохранить онтологию
        destroy_entity(stud)  # удаляем сущность студента
        return trajectory_disc

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT user_id, login, role_id FROM users WHERE user_id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False
            return res
        except OperationalError as e:
            print(f"Ошибка получения данных '{e}'")
        return False

    def getFullName(self, user_id):
        try:
            self.__cur.execute(f"SELECT record_book_number, full_name, user_id FROM student WHERE user_id = {user_id}")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False
            return res
        except OperationalError as e:
            print(f"Ошибка получения данных '{e}'")
        return False

    def getUserByLogin(self, login):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE login = '{login}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False
            return res
        except OperationalError as e:
            print(f"Ошибка получения данных '{e}'")
        return False
