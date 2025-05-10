from app.repositories.database import db

class BookLoan(db.Model):
    __tablename__ = 'book_loan'
    
    id = db.Column(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    id_loan = db.Column(db.Integer, db.ForeignKey('loans.id'), nullable=False)
    book_quantity = db.Column(db.Integer, default=1)
    
    def __repr__(self):
        return f'<BookLoan book:{self.id_book} loan:{self.id_loan}>'