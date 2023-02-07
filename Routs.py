from flask import Flask, render_template, redirect, session, url_for, request
import MakeTrajectory
from flask_login import LoginManager
import Connection as cn
import FDataBase as fdb


#login_manager = LoginManager()
app = Flask(__name__)
#login_manager.init_app(app)
# Set the secret key to some random bytes. Keep this really secret!
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    db = cn.get_db()
    dbase = fdb.FDataBase(db)

    return render_template('index.html', title='Диплом', disciplines = dbase.get_all_disciplines())
    #if 'username' in session:
        #return f'Logged in as {session["username"]}'
    #return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))




@app.route('/', methods=['GET', 'POST'])
def choice_of_disciplines():
    if request.method == 'POST':
        result = request.form.getlist('my_checkbox')  # выбранные дисциплины
        print(result)

        db = cn.get_db()
        dbase = fdb.FDataBase(db)

        trajectories = dbase.get_trajectory(result) # полученные траектории
        print(trajectories)

    return render_template('trajectory.html', trajectories=trajectories)


@app.route('/trajectory', methods=['GET'])
def trajectory():
    pass


app.run(debug=True)
