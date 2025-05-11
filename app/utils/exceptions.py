class ValidationError(Exception):
    """Erro de validação de dados"""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(message)

class BusinessRuleError(Exception):
    """Erro nas regras de negócio"""
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class NotFoundError(Exception):
    """Recurso não encontrado"""
    def __init__(self, message):
        self.message = message
        super().__init__(message)