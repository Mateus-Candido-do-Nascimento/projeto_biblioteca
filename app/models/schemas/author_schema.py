from marshmallow import Schema, fields, validate

class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)  # Apenas para saída
    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100, error="Nome deve ter entre 2 e 100 caracteres")
    )
    biography = fields.Str(validate=validate.Length(max=500))