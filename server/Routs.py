from flask import Flask, render_template, redirect, session, url_for, request, jsonify, make_response
import Connection as cn
import FDataBase as fdb
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import UploadProtegeFile
import jwt


app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

CORS(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cur_us')
def get_posts():

    current_user = {
        'id': 1,
        'login': 'login',
        'password': '12334',
        'full_name': 'Копыльских Виктория Максимовна',
        'rec_book_num': 23432335,
        'e_mail': 'lalala@test.ru'
    }
    print(current_user)
    return jsonify(current_user)


@app.route('/disciplines', methods=['GET', 'POST'])
#@login_required
def discipline():
    if request.method == 'GET':
        print(elective_disciplines)
        return jsonify(elective_disciplines)
    if request.method == 'POST':
        data_from_client = request.json
        print(data_from_client)
        trajectories = dbase.get_trajectory(data_from_client)  # полученные траектории
        print(trajectories)
        return jsonify(trajectories)
        #print(data_from_client)

        #data_from_client.clear()
        #print(trajectories)
        # Делаем что-то с полученными данными
        #return jsonify(trajectories)


@app.route('/trajectory', methods=['GET'])
def trajectory():
    return render_template('discipline.html', b_disciplines = basic_disciplines, e_disciplines = elective_disciplines)


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    print(username)
    print(password)

    user_data = dbase.check_and_get_user(username, password)
    print(type(user_data))
    if len(user_data) > 0:
        payload = {'username': username, 'password': password}
        token = jwt.encode(payload, 'my_secret_key', algorithm='HS256')
        return jsonify({'token': token})
    else:
        make_response('нет такого чела', 401)
    print(user_data)
    # Здесь происходит проверка логина и пароля на соответствие в базе данных
    # Если они верны, создаем токен и возвращаем его клиенту




@app.route('/logout')
def logout():
    print('пользователь пока')
    #session.clear()
    return redirect(url_for('login'))




@app.route('/profile', methods=['GET', 'POST'])
def profile():
    pass


@app.route('/student/all')
def get_all_stud():
    if request.method == 'GET':
        all_students = dbase.get_all_students()
        return jsonify(all_students)



@app.before_first_request
def before_first_request():
    session.clear()
    #print('before_first_request() called')


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением"""
    global dbase, basic_disciplines, elective_disciplines
    db = cn.get_db()
    dbase = fdb.FDataBase(db)

    basic_disciplines = dbase.get_basic_disciplines()
    elective_disciplines = dbase.get_elective_disciplines()

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
