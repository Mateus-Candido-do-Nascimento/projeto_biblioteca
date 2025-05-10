from app.repositories.database import db

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, default=1)
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    id_category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    loans = db.relationship('BookLoan', backref='book', lazy=True)
    
    def __repr__(self):
        return f'<Book {self.name}>'