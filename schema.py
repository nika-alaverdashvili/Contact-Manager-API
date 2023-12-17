from marshmallow import Schema, fields, validate


class ContactSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(max=128))
    name = fields.String(required=True, validate=validate.Length(max=256))
    lastname = fields.String(required=True, validate=validate.Length(max=256))
    phone = fields.Integer()
    gmail = fields.Email(required=True, validate=validate.Length(max=256))
    address = fields.String(validate=validate.Length(max=256))

    class Meta:
        # Set unknown to 'exclude' as a string
        unknown = 'exclude'
