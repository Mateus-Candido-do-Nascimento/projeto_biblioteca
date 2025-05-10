from marshmallow import Schema, fields, validate

class BookLoanSchema(Schema):
    id = fields.Int(dump_only=True)
    id_book = fields.Int(required=True)
    id_loan = fields.Int(required=True)
    book_quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Quantidade deve ser pelo menos 1")
    )