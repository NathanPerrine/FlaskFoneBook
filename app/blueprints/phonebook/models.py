from app import db

class PhoneBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    phone_number = db.Column(db.String(14), nullable = False)
    address = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Phone Book | {self.first_name}, {self.phone_number}>"
    def __str__(self):
        fullname = self.first_name
        if self.last_name:
            fullname += " " + self.last_name
        return f"{fullname}"