from app import db
from datetime import datetime

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, default=datetime.utcnow)
    end = db.Column(db.DateTime)
    
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id'))
    
    books = db.relationship('BookLoan', backref='loan', lazy='dynamic')
    
    def __repr__(self):
        return f'<Loan {self.id}>'

class BookLoan(db.Model):
    __tablename__ = 'book_loan'
    
    id = db.Column(db.Integer, primary_key=True)
    book_quantity = db.Column(db.Integer, default=1)
    
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'))
    id_loan = db.Column(db.Integer, db.ForeignKey('loans.id'))
    
    def __repr__(self):
        return f'<BookLoan {self.id}>'