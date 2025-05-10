from datetime import datetime, timedelta
from app.repositories import LoanRepository, BookRepository, BookLoanRepository
from app.utils.exceptions import NotFoundError, BusinessRuleError

class LoanService:
    @staticmethod
    def create_loan(client_id, book_ids):
        loan_data = {
            'id_client': client_id,
            'start': datetime.utcnow(),
            'end': None
        }
        loan = LoanRepository.create(loan_data)
        
        for book_id in book_ids:
            if not BookRepository.get_by_id(book_id):
                raise NotFoundError(f"Livro ID {book_id} não encontrado")
            BookLoanRepository.add_to_loan(loan.id, book_id)
        
        return loan

    @staticmethod
    def finalize_loan(loan_id):
        if not (loan := LoanRepository.get_by_id(loan_id)):
            raise NotFoundError("Empréstimo não encontrado")
        
        if loan.end:
            raise BusinessRuleError("Empréstimo já finalizado")
        
        return LoanRepository.finalize(loan_id)