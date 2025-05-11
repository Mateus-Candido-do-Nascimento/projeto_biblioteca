# Importa todos os Blueprints dos controllers
from .author_controller import author_bp
from .book_controller import book_bp
from .category_controller import category_bp
from .client_controller import client_bp
from .loan_controller import loan_bp

# Lista todos os Blueprints disponíveis
__all__ = [
    'author_bp',
    'book_bp',
    'category_bp',
    'client_bp',
    'loan_bp'
]