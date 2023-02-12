import json
from owlready2 import *
from psycopg2 import OperationalError
import MyOntology
from flask_login import current_user

with open('data.json', encoding='utf-8') as json_file:
    dictionary = json.load(json_file)


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

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
        disciplines_query = """SELECT discipline_name
            FROM basic_discipline;"""
        try:
            result = self.execute_query_select(disciplines_query)
            result_list = []
            for item in result:
                result_list.append(str(item[0]))
            return result_list
        except:
            print('Ошибка чтения из бд')
            return []

    def get_elective_disciplines(self):  # получить все дисциплины (без семестров)
        disciplines_query = """SELECT discipline_name
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

    def get_all_disciplines_with_semester(self):
        disciplines_query = """SELECT discipline_name, taught_per_semester
            FROM basic_discipline
            UNION SELECT discipline_name, taught_per_semester
            FROM elective_discipline
            ORDER by taught_per_semester;"""
        disciplines_result = self.execute_query_select(disciplines_quФery)
        return disciplines_result

    def get_trajectory(self, chosen_discipline):
        st_num = current_user.get_id()
        stud = MyOntology.Student('Student_' + str(st_num), None,
                                  full_name=[current_user.get_name()],
                                  record_book_number=[int(current_user.get_record_book_number())])
        stud.label = locstr('Студент ' + str(st_num), lang="ru")
        owlready2.sync_reasoner_pellet()  # запуск решателя

        for choos_disc in chosen_discipline:
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
            trajectory_disc[str(stud_trajec.label[0])] = cont_disc_list  # траектория и предметы в траектории (было str(stud_trajec.label[0])
            trajectory_list_for_db.append(stud_trajec.name)

        delete_query = f"DELETE FROM student_trajectories WHERE student_id = {current_user.get_record_book_number()}"
        self.execute_query(delete_query)

        print(trajectory_list_for_db)
        for tr in trajectory_list_for_db:
            query_for_insert_trajectory = f"INSERT INTO student_trajectories(student_id, trajectory_id) " \
                                          f"VALUES ({current_user.get_record_book_number()}, {tr})"
            self.execute_query(query_for_insert_trajectory)
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
