# flask_wtf - имя расширения flask-wtf для flask в команде импорта
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from wtforms.validators import ValidationError, Email, EqualTo


class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


# class RegisterForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password_repeat = PasswordField('Repeat password', validators=[DataRequired()])
#     submit = SubmitField('register')
