from flask import Flask,render_template, request, session, Response, redirect, url_for
from flask_login import login_manager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from database import connector
from forms import LoginForm, RegisterForm
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/')

def main():
    return render_template('index.html')

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - L O G I N - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/login", methods=['GET', 'POST'])
def login():
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
