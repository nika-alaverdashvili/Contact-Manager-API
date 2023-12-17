from db import db


class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(256), nullable=False)
    lastname = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    gmail = db.Column(db.String(256), unique=True, nullable=False)
    address = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f"<Contact {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "lastname": self.lastname,
            "phone": self.phone,
            "gmail": self.gmail,
            "address": self.address
        }
