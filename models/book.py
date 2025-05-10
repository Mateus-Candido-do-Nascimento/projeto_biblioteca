from app import db

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, default=0)
    
    # Relacionamentos
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('Author', backref='books')
    
    id_category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref='books')
    
    loans = db.relationship('BookLoan', backref='book', lazy='dynamic')
    
    def __repr__(self):
        return f'<Book {self.name}>'