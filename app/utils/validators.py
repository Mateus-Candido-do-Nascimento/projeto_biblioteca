from datetime import datetime
import re
from marshmallow import ValidationError

def validate_date_not_past(value):
    """Valida se a data não está no passado"""
    if value and value < datetime.now():
        raise ValidationError("A data não pode ser no passado")

def validate_quantity(value):
    """Valida se a quantidade é positiva"""
    if value < 0:
        raise ValidationError("A quantidade não pode ser negativa")

def validate_brazilian_phone(value):
    """Valida formato de telefone brasileiro"""
    if not re.match(r'^(\+55)?\s?(\(\d{2}\)\s?)?\d{4,5}[\s-]?\d{4}$', value):
        raise ValidationError("Telefone inválido. Use o formato (XX) XXXX-XXXX")

def validate_cpf(value):
    """Valida CPF brasileiro"""
    cpf = re.sub(r'[^\d]', '', value)
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido")
    
    # Cálculo dos dígitos verificadores
    for i in range(9, 11):
        digit = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        digit = (11 - (digit % 11)) % 10
        if digit != int(cpf[i]):
            raise ValidationError("CPF inválido")