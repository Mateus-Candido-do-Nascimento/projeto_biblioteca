from app.repositories.database import db, BaseRepository
from app.models.entities.book import Book
from sqlalchemy.exc import SQLAlchemyError

class BookRepository(BaseRepository):
    @staticmethod
    def get_all():
        return Book.query.order_by(Book.name).all()

    @staticmethod
    def get_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def search(query):
        return Book.query.filter(
            Book.name.ilike(f'%{query}%') | 
            Book.description.ilike(f'%{query}%')
        ).all()

    @staticmethod
    def get_by_author(author_id):
        return Book.query.filter_by(id_author=author_id).all()

    @staticmethod
    def get_by_category(category_id):
        return Book.query.filter_by(id_category=category_id).all()

    @staticmethod
    def create(book_data):
        try:
            book = Book(**book_data)
            return BaseRepository.save(book)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def update_quantity(book_id, change):
        book = BookRepository.get_by_id(book_id)
        if not book:
            return None
        try:
            book.quantity += change
            return BaseRepository.save(book)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def update(book_id, book_data):
        book = BookRepository.get_by_id(book_id)
        if not book:
            return None
        try:
            for key, value in book_data.items():
                setattr(book, key, value)
            return BaseRepository.save(book)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e