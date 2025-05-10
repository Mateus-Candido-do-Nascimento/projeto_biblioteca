from app.repositories.database import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    # Relacionamento 1:N com livros
    books = db.relationship('Book', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'