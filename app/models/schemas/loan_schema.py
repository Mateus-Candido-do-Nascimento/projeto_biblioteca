from marshmallow import Schema, fields, validates
from datetime import datetime
from app.utils.validators import ValidationError

class LoanSchema(Schema):
    id = fields.Int(dump_only=True)
    id_client = fields.Int(required=True)
    start = fields.DateTime(dump_only=True)  # Definido automaticamente
    end = fields.DateTime(allow_none=True)
    expected_end = fields.DateTime(allow_none=True)

    @validates('end')
    def validate_end_date(self, value):
        if value and value < datetime.now():
            raise ValidationError("Data final não pode ser no passado")

    @validates('expected_end')
    def validate_expected_end_date(self, value):
        if value and value < datetime.now():
            raise ValidationError("Data prevista de devolução não pode ser no passado")