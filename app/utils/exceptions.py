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