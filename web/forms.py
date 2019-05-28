
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('email', validators = [InputRequired(),Email()])
    password = PasswordField('password', validators= [InputRequired(), Length(min = 8, max = 80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    firstName = StringField('firstName', validators=[InputRequired(), Length(max=30)])
    lastName = StringField('lastName', validators=[InputRequired(), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

