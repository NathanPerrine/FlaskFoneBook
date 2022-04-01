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

@pb.route('/edit-contact/<contact_id>', methods=["GET", "POST"])
@login_required 
def edit_contact(contact_id):
    contact = PhoneBook.query.get_or_404(contact_id)
    #Check if the user trying to edit the post is the current user
    if contact.author != current_user:
        flash("You do not have edit access for this contact.", "danger")
        return redirect(url_for('phonebook.myphonebook'))
    title = f"Edit Contact: {{ contact.first_name }}"
    form = PhoneBookForm()
    if form.validate_on_submit():
        contact.update(**form.data)
        flash(f"{contact.first_name} has been updated.", "success")
        return redirect(url_for('phonebook.myphonebook'))
    return render_template('contact_edit.html', title=title, contact=contact, form=form)

@pb.route('/delete_contact/<contact_id>')
@login_required
def delete_contact(contact_id):
    contact = PhoneBook.query.get_or_404(contact_id)
    if contact.author != current_user:
        flash("You do not have delete access to this post.", 'secondary')
    else:
        contact.delete()
        flash(f"{contact} has been removed.", 'secondary')
    return redirect(url_for('phonebook.myphonebook'))