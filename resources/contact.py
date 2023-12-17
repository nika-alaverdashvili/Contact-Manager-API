from flask import jsonify
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError

from models.Contact import Contact
from schema import ContactSchema
from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView

blp = Blueprint("Contacts", __name__, description="Manipulations on contacts")


@blp.route("/contacts")
class ContactsView(MethodView):

    def get(self):
        contacts = Contact.query.all()
        contacts_data = [contact.to_dict() for contact in contacts]
        return jsonify(contacts_data)

    @blp.arguments(ContactSchema)
    @blp.response(201, ContactSchema)
    def post(self, args):
        """Create a new contact."""
        try:
            new_contact = Contact(**args)
            db.session.add(new_contact)
            db.session.commit()
            return new_contact.to_dict(), 201
        except ValidationError as e:
            db.session.rollback()
            abort(400, str(e.messages))
        except IntegrityError:
            db.session.rollback()
            abort(400, "Duplicate entry. This email or username already exists.")
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))


@blp.route("/contacts/<int:contact_id>")
class SingleContactView(MethodView):

    @blp.response(200, ContactSchema)
    def get(self, contact_id):
        contact = Contact.query.get_or_404(contact_id)
        return contact

    @blp.arguments(ContactSchema)
    @blp.response(200, ContactSchema)
    def put(self, args, contact_id):
        """Update a single contact."""
        try:
            # Remove 'id' field from the payload
            args.pop('id', None)

            contact = Contact.query.get_or_404(contact_id)
            for field, value in args.items():
                setattr(contact, field, value)
            db.session.commit()

            return contact.to_dict()
        except ValidationError as e:
            db.session.rollback()
            abort(400, str(e.messages))
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))

    @blp.response(204)
    def delete(self, contact_id):
        """Delete a single contact."""
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return {"message": "Successfully Deleted"}, 204

