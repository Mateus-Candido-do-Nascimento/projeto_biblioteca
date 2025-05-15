from datetime import datetime
from app.repositories.database import db

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    start = db.Column(db.DateTime, default=datetime.utcnow)
    end = db.Column(db.DateTime)
    expected_end = db.Column(db.DateTime)
    
    # Relacionamento N:N com livros (através de book_loan)
    books = db.relationship('BookLoan', backref='loan', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Loan {self.id}>'