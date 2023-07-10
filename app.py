from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
import os.path

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(base_dir, 'contacts.data')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


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
        return f"<User {self.username}>"

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


with app.app_context():
    db.create_all()


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/main", methods=["POST"])
def create_contact():
    data = request.get_json()
    required_fields = ["username", "name", "lastname", "gmail"]
    if not all(field in data for field in required_fields):
        abort(400, "Required fields are missing")

    new_contact = Contact(
        username=data.get("username"),
        name=data.get("name"),
        lastname=data.get("lastname"),
        phone=data.get("phone"),
        gmail=data.get("gmail"),
        address=data.get("address"))

    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": "Contact created"})


@app.route("/main", methods=["GET"])
def read_contacts():
    username = request.args.get("username")
    name = request.args.get("name")
    lastname = request.args.get("lastname")
    phone = request.args.get("phone")
    gmail = request.args.get("gmail")
    address = request.args.get("address")

    query = Contact.query
    if username:
        query = query.filter(Contact.username.contains(username))
    if name:
        query = query.filter(Contact.name.contains(name))
    if lastname:
        query = query.filter(Contact.lastname.contains(lastname))
    if phone:
        query = query.filter(Contact.phone.contains(phone))
    if gmail:
        query = query.filter(Contact.gmail.contains(gmail))
    if address:
        query = query.filter(Contact.address.contains(address))

    contacts = query.all()
    result = [contact.to_dict() for contact in contacts]
    return jsonify({'contacts': result})


@app.route("/main/<int:contact_id>", methods=["PUT"])
def update_contact(contact_id):
    data = request.get_json()
    contact = Contact.query.get(contact_id)

    if not contact:
        abort(404, "Contact not found")
    if "username" in data:
        contact.username = data["username"]
    if "name" in data:
        contact.name = data["name"]
    if "lastname" in data:
        contact.lastname = data["lastname"]
    if "phone" in data:
        contact.phone = data["phone"]
    if "gmail" in data:
        contact.gmail = data["gmail"]
    if "address" in data:
        contact.address = data["address"]

    db.session.commit()
    return jsonify({"message": "Contact updated successfully"})


@app.route("/main/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)

    if not contact:
        abort(404, "Contact not found")
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
