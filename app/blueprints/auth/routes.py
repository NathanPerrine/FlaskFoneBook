from flask import render_template, redirect, url_for, flash 
from flask_login import login_user, logout_user, login_required
from . import auth
from .forms import SignUpForm, LogInForm
from .models import User


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    title = "Sign Up"
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data 
        
        # Check if user exists
        user_already_exists = User.query.filter((User.username==username)|(User.email==email)).all()
        #User.query.filter(User.username.ilike('jimbim')).first()
        if user_already_exists:
            # If that username/email is already taken, flash a warning message, redirect
            flash("That username or email already exists, please try another.", "danger")
            return render_template('signup.html', title = title, form = form)

        new_user = User(email = email, username = username, password = password)
        flash(f"{new_user} has been created!")
        #set to login instead of redirect
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('signup.html', title = title, form = form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = "Log In"
    form = LogInForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data 
        # Check for a user with that username and then check the password
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f'{user} has successfully logged in.', 'success')
            return redirect(url_for('phonebook.index'))
        else: # No user or password is incorrect
            flash('Username and/or password is incorrect.', 'danger')

    return render_template('login.html', title = title, form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.', 'primary')
    return redirect(url_for('phonebook.index'))