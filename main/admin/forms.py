from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,EqualTo
from wtforms.fields import EmailField

class RegisterForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('password2', message='Password must much')])
    password2 = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('password2', message='Password must much')])
    password2 = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')
