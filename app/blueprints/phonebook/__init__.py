from flask import Blueprint

phonebook = Blueprint('phonebook', __name__, url_prefix='/pb')


from . import routes, models