from flask import render_template
from . import main
from .forms import *


@main.app_context_processor
def inject_values():
    return dict(
        login_form=LoginForm())


@main.route('/')
def index():
    return render_template('index.html')
