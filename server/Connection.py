import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")
    except OperationalError as error:
        print(f"The error '{error}' occurred")
    return connection


connection = create_connection("db_diploma", "postgres", "root", "127.0.0.1", "5432")


def get_db():
    return connection


def execute_query(query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
        #connection.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        #connection.close()


def execute_query_SELECT(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        #connection.close()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        #connection.close()

# connection = create_connection("db_diploma", "postgres", "root", "127.0.0.1", "5432")
