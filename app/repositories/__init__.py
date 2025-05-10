from .author_repository import AuthorRepository
from .book_repository import BookRepository
from .category_repository import CategoryRepository  # Adicionado
from .client_repository import ClientRepository
from .loan_repository import LoanRepository
from .book_loan_repository import BookLoanRepository

__all__ = [
    'AuthorRepository',
    'BookRepository',
    'CategoryRepository',  # Adicionado
    'ClientRepository',
    'LoanRepository',
    'BookLoanRepository'
]