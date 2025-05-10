from marshmallow import Schema, fields, validate
from marshmallow.validate import OneOf

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=2, max=50),
            validate.Regexp(r'^[a-zA-ZÀ-ÿ\s]*$', error="Aceita apenas letras e espaços")
        ]
    )