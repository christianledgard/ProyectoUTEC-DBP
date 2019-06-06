from flask import Flask,render_template, request, session, Response, redirect, url_for
from flask_login import login_manager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - L O G I N - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/authenticate', methods = ["POST"])
def authenticate():
    message = json.loads(request.data)
    email = message['email']
    password = message['password']
    #2. look in database
    db_session = db.getSession(engine)
    try:
        user = db_session.query(entities.Users
            ).filter(entities.Users.email == email
            ).filter(entities.Users.password == password
            ).one()
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')


# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - -  C R E A T E - U S E R - - - - -  - #
# - - - - - - - - - - - - - - - - - - - - - - - #




# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - -  C R U D - U S E R S  - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Users)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/users', methods = ['POST'])
def post_users():
    c =  json.loads(request.form['values'])
    user = entities.Users(
        firstName =c['firstName'],
        lastName =c['lastName'],
        password =c['password'],
        email =c['email']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return 'Created User'

@app.route('/users', methods = ['PUT'])
def update_users():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.Users).filter(entities.Users.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(user, key, c[key])
    session.add(user)
    session.commit()
    return 'Updated User'

@app.route('/users', methods = ['DELETE'])
def delete_user():
    id = request.form['key']
    session = db.getSession(engine)
    messages = session.query(entities.Users).filter(entities.Users.id == id)
    for message in messages:
        session.delete(message)
    session.commit()
    return "User Deleted"\


# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - -  O L D - M E T H O D  - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/loginold", methods=['GET', 'POST'])
def loginold():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(email=form.email.data, firstName=form.firstName.data, lastName=form.lastName.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('register.html', form=form)


@app.route("/inscripcion")
def inscripcion():
    return render_template('form1.html')



if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug=True,port=8020, threaded=True, host=('0.0.0.0'))
