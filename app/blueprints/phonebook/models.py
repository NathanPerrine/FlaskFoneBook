from app import db
import os 
import cloudinary
import cloudinary.uploader 
import cloudinary.api

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

class PhoneBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    phone_number = db.Column(db.String(14), nullable = False)
    address = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_url = db.Column(db.String(100))

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

    def update(self, **kwargs):
        for key, value in kwargs.items():
            # print(key, value)
            if key in {'first_name', 'last_name', 'phone_number', 'address'}:
                setattr(self, key, value)
            # if key == 'image':
            #     self.upload_to_cloudinary(value)
            db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def upload_to_cloudinary(self, file_to_upload):
        image_info = cloudinary.uploader.upload(file_to_upload)
        self.image_url = image_info.get('url')
        db.session.commit()