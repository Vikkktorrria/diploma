from flask import Flask, render_template, redirect, session, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
import Connection as cn
import FDataBase as fdb
from werkzeug.security import generate_password_hash, check_password_hash
import UploadProtegeFile


login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@login_manager.user_loader
def load_user(user_id):
    print("load user")
    return UserLogin().fromDB(user_id, dbase)


@app.route('/')
def index():
    return render_template('index.html', title='Диплом', disciplines = dbase.get_all_disciplines())
    #if 'username' in session:
        #return f'Logged in as {session["username"]}'
    #return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = dbase.getUserByLogin(request.form['login'])
        print("текущий юзер", user)
        if user and check_password_hash(user[2], request.form['psw']):
            userLogin = UserLogin().create(user)
            login_user(userLogin)
            flash("Вы успешно вошли!", "succes")
            return redirect(url_for('profile'))
        flash("Неверная пара логин/пароль", "error")
    return render_template("login.html")



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    return f"""<p><a href="{url_for('logout')}">Выйти из профиля</a>
                                            <p>Здравствуйте, {current_user.get_name()}"""




@app.route('/', methods=['GET', 'POST'])
def choice_of_disciplines():
    if request.method == 'POST':
        result = request.form.getlist('my_checkbox')  # выбранные дисциплины
        print(result)
        trajectories = dbase.get_trajectory(result) # полученные траектории
        print(trajectories)

    return render_template('trajectory.html', trajectories=trajectories)


@app.route('/trajectory', methods=['GET'])
def trajectory():
    pass


@app.before_first_request
def before_first_request():

    print('before_first_request() called')


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением"""
    global dbase
    db = cn.get_db()
    dbase = fdb.FDataBase(db)
    print('before_request() called')


@app.after_request
def after_request(response):
    print('after_request() called')
    return response


@app.teardown_request
def teardown_request(response):
    print('teardown_request() called')
    return response

app.run(debug=True)
