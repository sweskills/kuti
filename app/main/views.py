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
@main.route('/school/<int:id>')
def school_profile(id):
        school = School.query.filter_by(id=id).first()
        return render_template('school_profile.html', school=school)

@login_required
@main.route('/teacher/<int:id>')
def teacher_profile(id):
        teacher = Teacher.query.filter_by(id=id).first()
        return render_template('teacher_profile.html', teacher=teacher)
