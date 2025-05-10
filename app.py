from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa o db
    db.init_app(app)
    
    # Importa TODOS os modelos ANTES de criar as tabelas
    from models.book import Book
    from models.author import Author
    from models.category import Category
    from models.loan import Loan, BookLoan
    
    with app.app_context():
        # Cria todas as tabelas
        db.create_all()
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)