from app.repositories.database import db

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.Text)
    
    # Relacionamento 1:N com livros
    books = db.relationship('Book', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<Author {self.name}>'