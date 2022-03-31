from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import PhoneBookForm, SignUpForm, LogInForm
from app.models import PhoneBook, User

@app.route('/')
def index():
    phonebooks = PhoneBook.query.all()
    title = 'home'
    return render_template('index.html', title = title, pb = phonebooks)



@app.route('/phonebook', methods = ["GET", "POST"])
@login_required
def phonebook():
    title = 'phone book entry'
    form = PhoneBookForm()

    if form.validate_on_submit():
        first_name = form.first_name.data 
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data 
        new_pbook = PhoneBook(first_name = first_name, last_name = last_name, phone_number = phone_number, address = address)

        return redirect(url_for('phonebook'))

    return render_template('phonebook.html', title = title, form = form)

@app.route('/myphonebook')
@login_required
def myphonebook():
    title = "My PhoneBook Entries"
    books = current_user.phonebooks.all()
    return render_template('my_phonebook.html', title = title, books = books)


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    title = "Sign Up"
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data 
        
        # Check if user exists
        user_already_exists = User.query.filter((User.username==username)|(User.email==email)).all()
        if user_already_exists:
            # If that username/email is already taken, flash a warning message, redirect
            flash("That username or email already exists, please try another.", "danger")
            return render_template('signup.html', title = title, form = form)

        new_user = User(email = email, username = username, password = password)
        flash(f"{new_user} has been created!")
        
        return redirect(url_for('login'))
    return render_template('signup.html', title = title, form = form)


@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('index'))
        else: # No user or password is incorrect
            flash('Username and/or password is incorrect.', 'danger')

    return render_template('login.html', title = title, form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out.', 'primary')
    return redirect(url_for('index'))