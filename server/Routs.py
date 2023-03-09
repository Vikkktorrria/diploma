from flask import Flask, render_template, redirect, session, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
import Connection as cn
import FDataBase as fdb
from werkzeug.security import generate_password_hash, check_password_hash
import UploadProtegeFile



app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Прежде чем посетить данную страницу, вам необходимо авторизоваться'
login_manager.login_message_category = "success"
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@login_manager.user_loader
def load_user(user_id):
     print("load user")
     print(user_id)
     return UserLogin().fromDB(user_id, dbase)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/discipline', methods=['GET', 'POST'])
@login_required
def discipline():
    if request.method == 'GET':
        basic_disciplines = dbase.get_basic_disciplines()
        elective_disciplines = dbase.get_elective_disciplines()
        return render_template('discipline.html', b_disciplines = basic_disciplines, e_disciplines = elective_disciplines)
    if request.method == 'POST':
        result = request.form.getlist('my_checkbox')  # выбранные дисциплины
        print(result)
        trajectories = dbase.get_trajectory(result)  # полученные траектории
        result.clear()
        print(trajectories)
        return render_template('trajectory.html', trajectories=trajectories)

@app.route('/trajectory', methods=['GET'])
def trajectory():
    basic_disciplines = dbase.get_basic_disciplines()
    elective_disciplines = dbase.get_elective_disciplines()
    return render_template('discipline.html', b_disciplines = basic_disciplines, e_disciplines = elective_disciplines)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        user = dbase.getUserByLogin(request.form['login'])
        if user and check_password_hash(user[2], request.form['psw']):
            userLogin = UserLogin().create(user)
            login_user(userLogin)
            return redirect(request.args.get("next") or url_for('profile'))
        flash("Неверная пара логин/пароль", "error")
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    print('пользователь пока')
    #session.clear()
    return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET':
        return render_template('profile.html', user_full_name = current_user.get_name())
    if request.method == 'POST':
        return redirect(url_for('logout'))





@app.before_first_request
def before_first_request():
    session.clear()
    #print('before_first_request() called')


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением"""
    global dbase
    db = cn.get_db()
    dbase = fdb.FDataBase(db)
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
