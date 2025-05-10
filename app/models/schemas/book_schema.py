from marshmallow import Schema, fields, validate
from marshmallow import validates_schema, ValidationError

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100)
    )
    description = fields.Str(validate=validate.Length(max=500))
    quantity = fields.Int(validate=validate.Range(min=0))
    id_author = fields.Int(required=True)
    id_category = fields.Int(required=True)

    @validates_schema
    def validate_quantity(self, data, **kwargs):
        if 'quantity' in data and data['quantity'] < 0:
            raise ValidationError("Quantidade não pode ser negativa", "quantity")