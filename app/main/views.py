from flask import render_template
from . import main
from .forms import *
from ..models import *
from flask_login import login_required, current_user

from ..models import *
from  .. import db 


@main.app_context_processor
def inject_values():
    return dict(
        login_form=LoginForm()        
        )

@main.route('/')
def index():
    return render_template('index.html')


@login_required
@main.route('/school')
def school_Profile():
        school = School.query.first()
        return render_template('school_Profile.html', school=school)
