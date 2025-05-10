from app.repositories.database import db, BaseRepository
from app.models.entities.author import Author
from sqlalchemy.exc import SQLAlchemyError

class AuthorRepository(BaseRepository):
    @staticmethod
    def get_all():
        return Author.query.order_by(Author.name).all()

    @staticmethod
    def get_by_id(author_id):
        return Author.query.get(author_id)

    @staticmethod
    def get_by_name(name):
        return Author.query.filter(Author.name.ilike(f'%{name}%')).all()

    @staticmethod
    def create(author_data):
        try:
            author = Author(**author_data)
            return BaseRepository.save(author)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def update(author_id, author_data):
        author = AuthorRepository.get_by_id(author_id)
        if not author:
            return None
            
        try:
            for key, value in author_data.items():
                setattr(author, key, value)
            return BaseRepository.save(author)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def delete(author_id):
        author = AuthorRepository.get_by_id(author_id)
        if not author:
            return False
            
        try:
            db.session.delete(author)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e