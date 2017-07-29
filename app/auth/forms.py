from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')



class schoolRegistrationForm(Form):
    email = StringField('Email',
                                validators=[Required(), Length(min=7, max=64)
                                ])
    password = PasswordField('New Password', validators=[
                    Required(),
                    EqualTo('Confirm Password', message='Passwords must match')
                    ])
    confirmPassword = PasswordField('Confirm Password', validators=[
                        Required(), EqualTo('password', message='password must match')
                        ])
    register = SubmitField('Register')
