from flask import render_template, redirect, request, url_for, flash
from . import auth
from . forms import *
from flask_login import current_user,\
        login_user, login_required, logout_user


@auth.app_context_processor
def inject_values():
    return dict(
        login_form=LoginForm()
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
