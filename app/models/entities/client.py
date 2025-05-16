from app.repositories.database import db

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    
    loans = db.relationship('Loan', backref='client', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Client {self.name}>'

    @property
    def active_loans_count(self):
        # Considera empréstimos ativos aqueles sem data de devolução (end == None)
        return sum(1 for loan in self.loans if loan.end is None)