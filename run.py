from app import app, db
from app.blueprints.auth.models import User
from app.blueprints.phonebook.models import PhoneBook

@app.shell_context_processor
def make_context():
    return {'db':db, 'PhoneBook': PhoneBook, 'User':User}