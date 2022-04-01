from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

class PhoneBookForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name  = StringField('Last Name')
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    image = FileField('Post Image')
    submit = SubmitField('Add')