from datetime import datetime, timedelta
from app.repositories import LoanRepository, BookRepository, BookLoanRepository
from app.utils.exceptions import NotFoundError, BusinessRuleError

class LoanService:
    @staticmethod
    def create_loan(client_id, book_ids, expected_end_date=None):
        expected_end_dt = None
        if expected_end_date:
            expected_end_dt = datetime.strptime(expected_end_date, "%Y-%m-%d")
            # Validação: data prevista deve ser posterior à data atual
            if expected_end_dt.date() < datetime.utcnow().date():
                raise BusinessRuleError("A data prevista de devolução não pode ser anterior à data atual")
        
        loan_data = {
            'id_client': client_id,
            'start': datetime.utcnow(),
            'expected_end': expected_end_dt,
            'end': None
        }
        
        # Validação de quantidade de livros
        for book_id in book_ids:
            book = BookRepository.get_by_id(book_id)
            if not book:
                raise NotFoundError(f"Livro ID {book_id} não encontrado")
            if book.quantity <= 0:
                raise BusinessRuleError(f"Livro '{book.name}' não está disponível para empréstimo")
        
        loan = LoanRepository.create(loan_data)
        for book_id in book_ids:
            BookLoanRepository.add_to_loan(loan.id, book_id)
            BookRepository.update_quantity(book_id, -1)
        return loan

    @staticmethod
    def finalize_loan(loan_id):
        if not (loan := LoanRepository.get_by_id(loan_id)):
            raise NotFoundError("Empréstimo não encontrado")
        if loan.end:
            raise BusinessRuleError("Empréstimo já finalizado")
        
        # Verifica se está atrasado
        is_late = loan.expected_end and loan.expected_end.date() < datetime.utcnow().date()
        
        for book_loan in loan.books:
            BookRepository.update_quantity(book_loan.id_book, 1)
        
        from app.repositories.database import db
        loan.end = datetime.utcnow()
        db.session.commit()
        
        return loan, is_late

    @staticmethod
    def get_all_loans():
        from app.repositories import LoanRepository
        return LoanRepository.get_all()

    @staticmethod
    def delete_loan(loan_id):
        loan = LoanRepository.get_by_id(loan_id)
        if not loan:
            raise NotFoundError("Empréstimo não encontrado")
        # Se o empréstimo ainda não foi devolvido, devolve os livros
        if not loan.end:
            for book_loan in loan.books:
                BookRepository.update_quantity(book_loan.id_book, 1)
        return LoanRepository.delete(loan_id)

    @staticmethod
    def get_loan_by_id(loan_id):
        loan = LoanRepository.get_by_id(loan_id)
        if loan:
            return loan
        raise NotFoundError("Empréstimo não encontrado")