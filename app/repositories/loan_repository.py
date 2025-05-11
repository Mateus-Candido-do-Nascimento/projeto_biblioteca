from app.repositories.database import db, BaseRepository
from app.models.entities.loan import Loan
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class LoanRepository(BaseRepository):
    @staticmethod
    def get_all():
        return Loan.query.order_by(Loan.start.desc()).all()

    @staticmethod
    def get_active():
        return Loan.query.filter(Loan.end.is_(None)).all()

    @staticmethod
    def get_by_client(client_id):
        return Loan.query.filter_by(id_client=client_id).order_by(Loan.start.desc()).all()

    @staticmethod
    def create(loan_data):
        try:
            loan = Loan(**loan_data)
            return BaseRepository.save(loan)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def finalize(loan_id):
        loan = LoanRepository.get_by_id(loan_id)
        if not loan or loan.end:
            return None
            
        try:
            loan.end = datetime.utcnow()
            return BaseRepository.save(loan)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e