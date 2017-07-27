from flask import render_template
from . import main
from .forms import *

from ..models import *
from  .. import db 


@main.app_context_processor
def inject_values():
    return dict(
        login_form=LoginForm())


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/school')
def schools():
	schools =  School.query.all()
	return render_template('school.html', schools=schools)