from app.repositories.database import db

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    
    loans = db.relationship('Loan', backref='client', lazy=True)
    
    def __repr__(self):
        return f'<Client {self.name}>'