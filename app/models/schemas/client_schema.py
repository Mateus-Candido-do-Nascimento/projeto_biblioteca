from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class ClientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )
    email = fields.Email(required=True)
    phone = fields.Str(validate=validate.Length(max=20))

    @validates('email')
    def validate_email(self, value):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValidationError("Formato de email inválido")