from datetime import datetime
import re
from marshmallow import ValidationError

def validate_date_not_past(value):
    """Valida se a data não está no passado (para empréstimos)"""
    if value and value < datetime.now():
        raise ValidationError("A data não pode ser no passado")

def validate_quantity(value):
    """Valida se a quantidade é positiva (para livros)"""
    if value < 0:
        raise ValidationError("A quantidade não pode ser negativa")

def validate_email_format(value):
    """Valida o formato básico de email (para clients)"""
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        raise ValidationError("Formato de email inválido")