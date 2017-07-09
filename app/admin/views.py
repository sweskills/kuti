from flask import render_template, redirect, request, url_for, flash
from . import admin
from .forms import *
from flask_login import current_user,\
        login_user, login_required, logout_user
from ..decorators import admin_required



@admin.app_context_processor
def inject_values():
    return dict(
        LoginForm=LoginForm())


@admin.route('/')
@login_required
@admin_required
def index():
    return render_template("admin/admin.html")
