from marshmallow import Schema, fields, validate
from datetime import datetime

class LoanSchema(Schema):
    id = fields.Int(dump_only=True)
    id_client = fields.Int(required=True)
    start = fields.DateTime(dump_only=True)  # Definido automaticamente
    end = fields.DateTime(allow_none=True)

    @validates('end')
    def validate_end_date(self, value):
        if value and value < datetime.now():
            raise ValidationError("Data final não pode ser no passado")