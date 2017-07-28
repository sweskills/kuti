from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError
from flask_bootstrap import Bootstrap

class LoginForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators = [Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')

class TeacherForm(Form):
	
    email= StringField('email',validators= [Required(),Length(min = 7, max = 64)]
    	)
    password = PasswordField('New Password',validators = [Required(),EqualTo('Confirm Password', message = 'message must match')])

    ConfirmPassword = PasswordField('Confirm Password', validators= [Required()])
    
    register = SubmitField('Register')

    	
