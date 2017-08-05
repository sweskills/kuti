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
@auth.route('/school_register', methods=['GET', 'POST'])
def register():
    form = SchoolRegistrationForm()
    if form.validate_on_submit():
        school = School(email=form.email.data,
                    password=form.password.data)
        db.session.add(school)
        db.session.commit()
        flash('School successfully registered')
        login_user(school.user)
        return redirect(url_for('auth.profile'))
    return render_template('register.html', form=form,
                           form_title="School")

#register teacher post request
@auth.route('/teacher_register', methods=['GET', 'POST'])
def teacher_register():
    form = TeacherRegistrationForm()
    if form.validate_on_submit():
        teacher = Teacher(email=form.email.data,
                    password=form.password.data)
        db.session.add(teacher)
        db.session.commit()
        flash('You have successfully registered')
        login_user(teacher.user)
        return redirect(url_for('auth.teacher_profile'))
    return render_template('register.html', form=form,
                           form_title="Teacher")

@login_required
@auth.route('/school_profile_form', methods=['GET', 'POST'])
def profile():
    school = School.query.filter_by(id=current_user.id).first()
    form = SchoolProfileForm(obj=school)
    if form.validate_on_submit():
        school.name = form.name.data
        school.location = form.location.data
        school.profile_form = form.profile_form.data
        school.address1 = form.address1.data
        school.address2 = form.address2.data
        school.website = form.website.data
        school.phone_number = form.phone_number.data
        db.session.add(school)
        db.session.commit()
        flash("Your details have been successfully submitted!")
        return redirect(url_for('main.school_profile', id=current_user.id))
    return render_template('profile.html', form=form)

@login_required
@auth.route('/teacher_profile_form', methods=['GET', 'POST'])
def teacher_profile():
    teacher = Teacher.query.filter_by(id=current_user.id).first()
    form = TeacherProfileForm(obj=teacher)
    if form.validate_on_submit():
        teacher.fullname = form.fullname.data
        teacher.location = form.location.data
        teacher.address1 = form.address1.data
        teacher.address2 = form.address2.data
        teacher.phone_number = form.phone_number.data
        teacher.sex = form.sex.data
        teacher.job_history = form.job_history.data
        teacher.educational_history = form.educational_history.data
        teacher.certifications = form.certifications.data
        teacher.references = form.references.data
        teacher.searching = form.searching.data
        db.session.add(teacher)
        db.session.commit()
        flash("Your details have been successfully submitted!")
        return redirect(url_for('main.teacher_profile', id=current_user.id))
    return render_template('profile.html', form=form)
