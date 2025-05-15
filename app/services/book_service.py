from app.repositories import BookRepository, AuthorRepository, CategoryRepository
from app.models.schemas import BookSchema
from app.utils.exceptions import NotFoundError, BusinessRuleError

class BookService:
    @staticmethod
    def get_all_books():
        return BookRepository.get_all()

    @staticmethod
    def get_book_by_id(book_id):
        if not (book := BookRepository.get_by_id(book_id)):
            raise NotFoundError("Livro não encontrado")
        return book

    @staticmethod
    def create_book(data):
        validated_data = BookSchema().load(data)
        
        # Verifica se autor e categoria existem
        if not AuthorRepository.get_by_id(validated_data['id_author']):
            raise NotFoundError("Autor não encontrado")
        if not CategoryRepository.get_by_id(validated_data['id_category']):
            raise NotFoundError("Categoria não encontrada")
        
        return BookRepository.create(validated_data)

    @staticmethod
    def update_book(book_id, data):
        if not BookRepository.get_by_id(book_id):
            raise NotFoundError("Livro não encontrado")
        
        validated_data = BookSchema().load(data, partial=True)
        return BookRepository.update(book_id, validated_data)

    @staticmethod
    def delete_book(book_id):
        if not BookRepository.get_by_id(book_id):
            raise NotFoundError("Livro não encontrado")
        return BookRepository.delete(book_id)

    @staticmethod
    def rent_book(book_id):
        book = BookService.get_book_by_id(book_id)
        
        if book.quantity <= 0:
            raise BusinessRuleError("Livro não está disponível para aluguel")
        
        return BookRepository.update_quantity(book_id, -1)

    @staticmethod
    def return_book(book_id):
        book = BookService.get_book_by_id(book_id)
        return BookRepository.update_quantity(book_id, 1)

    @property
    def is_available(self):
        return self.quantity > 0

    @staticmethod
    def update_quantity(book_id, change):
        if not (book := BookRepository.get_by_id(book_id)):
            raise NotFoundError("Livro não encontrado")
        
        if book.quantity + change < 0:
            raise BusinessRuleError("Quantidade não pode ficar negativa")
        
        return BookRepository.update_quantity(book_id, change)