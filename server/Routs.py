from flask import Flask, render_template, redirect, session, url_for, request, jsonify, make_response
import Connection as cn
import FDataBase as fdb
from flask_cors import CORS
import jwt


app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

CORS(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/disciplines', methods=['GET', 'POST'])
def discipline():
    if request.method == 'GET':
        print(elective_disciplines)
        return jsonify(elective_disciplines)
    if request.method == 'POST':
        data_from_client = request.json
        print('данные с клиента', data_from_client)
        choosen_disciplines = data_from_client['disciplines']

        student_data = data_from_client['student']
        user_id = student_data['user_id']
        rec_book_num = student_data['rec_book_num']
        surname = student_data['surname']
        name = student_data['name']
        patronymic = student_data['patronymic']
        f_name = surname + name + patronymic

        trajectories = dbase.get_trajectory(choosen_disciplines, user_id, rec_book_num, f_name)  # полученные траектории
        print('полученные траектории', trajectories)
        dbase.set_trajectories_to_student(trajectories, rec_book_num)  # добавляем траектории в бд


@app.route('/trajectory/my', methods=['GET'])
def stud_trajectories(stud_id):
    if request.method == 'GET':
        data_from_client = request.json
        print('Айди пользователя для которого нужно получить траектории', data_from_client)
        trajec = dbase.get_student_trajectories(stud_id)
        return jsonify(trajec)


# ================================  ВСЕ ДИСЦИПЛИНЫ, КОМПЕТЕНЦИИ, ТРАЕКТОРИИ, СТУДЕНТЫ ==============================
@app.route('/disciplines/all', methods=['GET', 'POST'])
def all_discipline():
    if request.method == 'GET':
        return jsonify(all_disciplines)


@app.route('/competences/all', methods=['GET', 'POST'])
def all_competences():
    if request.method == 'GET':
        return jsonify(all_competenses)


@app.route('/trajectory/all', methods=['GET'])
def all_trajectories():
    if request.method == 'GET':
        all_trajec = dbase.get_all_trajectories()
        return jsonify(all_trajec)


@app.route('/student/all')
def get_all_stud():
    if request.method == 'GET':
        all_students = dbase.get_all_students()
        return jsonify(all_students)
# =================================================================================================================


# ======================== вход и регистрация ================================
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    print(username)
    print(password)

    user_data = dbase.check_and_get_user(username, password)

    print(type(user_data))
    if user_data is not None:
        if user_data['role_id'] == 1:
            user_role = 'Регистратор'
        elif user_data['role_id'] == 2:
            user_role = 'Студент'
        else:
            pass

        print('роль', user_data['role_id'], user_role)
        payload = {'username': username, 'password': password}
        token = jwt.encode(payload, 'my_secret_key', algorithm='HS256')

       # return jsonify({'token': token})
        if user_role == 'Студент':
            return jsonify({
                'token': token,
                'user': {
                    'rec_book_num': user_data['record_book_number'],
                    'username': user_data['login'],
                    'surname': user_data['surname'],
                    'name': user_data['name'],
                    'patronymic': user_data['patronymic'],
                    'e_mail': user_data['e_mail'],
                    'user_id': user_data['user_id'],
                    'role_id': user_data['role_id'],
                }
            })
        if user_role == 'Регистратор':
            return jsonify({
                'token': token,
                'user': {
                    'username': user_data['login'],
                    'user_id': user_data['user_id'],
                    'role_id': user_data['role_id'],
                }
            })
    else:
        print('нет такого чела')
        #error = {'error': 'Неверный логин или пароль (ответ сервера)'}
        return make_response('ашибка', 401)
    # Здесь происходит проверка логина и пароля на соответствие в базе данных
    # Если они верны, создаем токен и возвращаем его клиенту


@app.route('/student/registration', methods=['POST'])
def stud_registration():
    student = request.json
    dbase.register_student(student)
    print(student)
    return make_response('всё ок', 200)

# =================================================================================




@app.before_first_request
def before_first_request():
    session.clear()
    #print('before_first_request() called')


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением"""
    global dbase, basic_disciplines, elective_disciplines, all_trajectories, all_disciplines, all_competenses
    db = cn.get_db()
    dbase = fdb.FDataBase(db)

    basic_disciplines = dbase.get_basic_disciplines()
    elective_disciplines = dbase.get_elective_disciplines()
    all_trajectories = dbase.get_all_trajectories()
    all_disciplines = dbase.get_all_disciplines()
    all_competenses = dbase.get_all_competences()


    #print('before_request() called')


@app.after_request
def after_request(response):
    #print('after_request() called')
    return response


@app.teardown_request
def teardown_request(response):
    #print('teardown_request() called')
    return response

app.run(debug=True)
