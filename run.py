from app import app, db
from app.models import PhoneBook

@app.shell_context_processor
def make_context():
    return {'db':db, 'PhoneBook': PhoneBook}