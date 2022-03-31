from . import phonebook as pb
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from .forms import PhoneBookForm
from .models import PhoneBook


@pb.route('/')
def index():
    phonebooks = PhoneBook.query.all()
    title = 'Home'
    return render_template('index.html', title = title, pb = phonebooks)



@pb.route('/phonebookentry', methods = ["GET", "POST"])
@login_required
def phonebookentry():
    title = 'phone book entry'
    form = PhoneBookForm()

    if form.validate_on_submit():
        first_name = form.first_name.data 
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data 
        new_pbook = PhoneBook(first_name = first_name, last_name = last_name, phone_number = phone_number, address = address, user_id = current_user.id)
        flash(f"{first_name} has been added to your PhoneBook.", "primary")
        return redirect(url_for('phonebook.phonebookentry'))

    return render_template('phonebookentry.html', title = title, form = form)

@pb.route('/myphonebook')
@login_required
def myphonebook():
    title = "My PhoneBook Entries"
    books = current_user.phonebooks.all()
    return render_template('my_phonebook.html', title = title, books = books)