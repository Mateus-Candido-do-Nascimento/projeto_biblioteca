from app.repositories.database import db, BaseRepository
from app.models.entities.book_loan import BookLoan
from sqlalchemy.exc import SQLAlchemyError

class BookLoanRepository(BaseRepository):
    @staticmethod
    def add_to_loan(loan_id, book_id, quantity=1):
        try:
            book_loan = BookLoan(
                id_loan=loan_id,
                id_book=book_id,
                book_quantity=quantity
            )
            return BaseRepository.save(book_loan)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def get_books_for_loan(loan_id):
        return BookLoan.query.filter_by(id_loan=loan_id).all()

    @staticmethod
    def remove_from_loan(loan_id, book_id):
        book_loan = BookLoan.query.filter_by(
            id_loan=loan_id,
            id_book=book_id
        ).first()
        
        if not book_loan:
            return False
            
        try:
            db.session.delete(book_loan)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e