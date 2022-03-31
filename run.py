from app import app, db
from app.models import PhoneBook, User

@app.shell_context_processor
def make_context():
    return {'db':db, 'PhoneBook': PhoneBook, 'User':User}