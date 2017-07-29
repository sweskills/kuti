from flask import render_template, redirect, request, url_for, flash, session
from . import auth
from .forms import *
from ..models import *
from flask_login import current_user,\
        login_user, login_required, logout_user
from flask_wtf import FlaskForm
from ..models import db


@auth.app_context_processor
def inject_values():
    return dict(
        login_form=LoginForm(),
        #register_form=schoolRegistrationForm()
        )


@auth.route('/register_teacher', methods=['GET','POST'])
def register():
    form = TeacherForm()
    if form.validate_on_submit():
        teacher = Teacher(email = form.data.get('email'),password = form.data.get('password'), 
            confirmed= form.data.get('confirmed'))
        db.session.add(teacher)
        db.session.commit()
        flash("Teacher was successfully registered")
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

    
@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        # if not current_user.confirmed\
        #     and request.endpoint[:5] != 'auth.':
        #     return redirect(url_for('auth.unconfirmed'))


@auth.route('/login', methods=['POST'])
def login():
    form = request.form
    user = User.query.filter_by(email=form.get("email", "")).first()
    if user is not None and user.verify_password(form.get("password","")):
        login_user(user, form.get("remember_me", ""))
        return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password')
    return redirect(request.args.get('next') or url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


#register school post request
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = schoolRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.email.data,
                    form.password.data)
        db_session.add(School)
        db.session.commit()
        flash('School successfully registered')
        return redirect(url_for('index.html'))
    return render_template('register.html', form=form)

@login_required
@auth.route('/profileform', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        school = School.query.filter_by(id=current_user.id).first()
        school.name = form.data.get("name")
        school.location = form.data.get("location")
        school.profile_form = form.data.get("profile_form")
        db.session.add(school)
        db.session.commit()
        flash("Your details have been successfully submitted!")
        return redirect(url_for('main.index'))
    return render_template('profile.html', form=form)

