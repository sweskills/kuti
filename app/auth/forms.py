from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField,\
 SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')


class SchoolRegistrationForm(Form):
    email = StringField('Email',
                                validators=[Required(), Length(min=7, max=64)
                                ])
    password = PasswordField('New Password', validators=[
                    Required()
                    ])
    confirmPassword = PasswordField('Confirm Password', validators=[
                        Required(), EqualTo('password', message='password must match')
                        ])
    register = SubmitField('Register')

class TeacherRegistrationForm(Form):
    email = StringField('Email',
                                validators=[Required(), Length(min=7, max=64)
                                ])
    password = PasswordField('New Password', validators=[
                    Required()
                    ])
    confirmPassword = PasswordField('Confirm Password', validators=[
                        Required(), EqualTo('password', message='password must match')
                        ])
    register = SubmitField('Register')

class SchoolProfileForm(Form):
    name = StringField('Name', validators=[Required()])
    location = StringField('Location', validators=[Required()])
    address1 = StringField('Address')
    address2 = StringField('Address 2')
    website = StringField('Website')
    phone_number = IntegerField('Phone number')
    profile_form = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')

class TeacherProfileForm(Form):
    fullname = StringField('Name', validators=[Required()])
    location = StringField('Location', validators=[Required()])
    sex = SelectField('Sex', choices=[(True, "Male"), (False, "Female")], coerce=bool)
    job_history = TextAreaField('Job History')
    educational_history = TextAreaField('Educational History')
    certifications = TextAreaField('Certifications')
    references = TextAreaField('References')
    searching = BooleanField('Searching for job?')
    address1 = StringField('Address')
    address2 = StringField('Address 2')
    phone_number = IntegerField('Phone number')
    submit = SubmitField('Submit')
