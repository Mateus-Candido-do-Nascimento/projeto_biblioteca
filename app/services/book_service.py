from app.repositories import BookRepository, AuthorRepository, CategoryRepository
from app.models.schemas import BookSchema
from app.utils.exceptions import NotFoundError, BusinessRuleError

class BookService:
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
    def update_quantity(book_id, change):
        if not (book := BookRepository.get_by_id(book_id)):
            raise NotFoundError("Livro não encontrado")
        
        if book.quantity + change < 0:
            raise BusinessRuleError("Quantidade não pode ficar negativa")
        
        return BookRepository.update_quantity(book_id, change)