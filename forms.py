from wtforms import StringField, SubmitField, PasswordField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange, EqualTo, Email

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField("Sign Me Up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"autocomplete": "username"})
    password = PasswordField("Password", validators=[DataRequired()],render_kw={"autocomplete": "current-password"})
    submit = SubmitField("Let Me In!")