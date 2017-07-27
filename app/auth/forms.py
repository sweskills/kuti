from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')


class ProfileForm(Form):
	name = StringField('Name', validators=[Required()])
	location = StringField('Location', validators=[Required()])
	profile_form = TextAreaField('Description', validators=[Required()])
	submit = SubmitField('Submit')