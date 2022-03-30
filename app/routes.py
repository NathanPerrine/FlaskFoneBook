from app import app
from flask import render_template, redirect, url_for
from app.forms import PhoneBookForm, SignUpForm
from app.models import PhoneBook
@app.route('/')
def index():
    phonebooks = PhoneBook.query.all()
    title = 'home'
    return render_template('index.html', title = title, pb = phonebooks)



@app.route('/phonebook', methods = ["GET", "POST"])
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

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    title = "Sign Up"
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data 
        
        print(email, username, password)
    
    return render_template('signup.html', title = title, form = form)