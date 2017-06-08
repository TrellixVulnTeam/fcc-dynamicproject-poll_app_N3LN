from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  username = StringField('Email', validators=[DataRequired("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired("Please enter your email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Login")

# New Poll Form