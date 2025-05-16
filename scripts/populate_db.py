import os
import sys

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.repositories.database import db
from app.models.entities import Author, Category, Book, Client, Loan, BookLoan
from datetime import datetime, timedelta

def populate_database():
    app = create_app()
    with app.app_context():
        # Limpa o banco
        db.drop_all()
        db.create_all()

        # Criar Autores
        autores = [
            Author(name='Machado de Assis'),
            Author(name='Clarice Lispector'),
            Author(name='Jorge Amado'),
            Author(name='Paulo Coelho'),
            Author(name='Monteiro Lobato'),
            Author(name='Carlos Drummond de Andrade'),
            Author(name='Graciliano Ramos'),
            Author(name='Eça de Queirós')
        ]
        for autor in autores:
            db.session.add(autor)
        db.session.commit()

        # Criar Categorias
        categorias = [
            Category(name='Romance'),
            Category(name='Ficção'),
            Category(name='Infantil'),
            Category(name='Poesia'),
            Category(name='Drama'),
            Category(name='Contos'),
            Category(name='Crônicas')
        ]
        for categoria in categorias:
            db.session.add(categoria)
        db.session.commit()

        # Criar Livros
        livros = [
            Book(name='Dom Casmurro', quantity=5, id_author=1, id_category=1),
            Book(name='Memórias Póstumas de Brás Cubas', quantity=3, id_author=1, id_category=1),
            Book(name='A Hora da Estrela', quantity=4, id_author=2, id_category=2),
            Book(name='Gabriela, Cravo e Canela', quantity=6, id_author=3, id_category=1),
            Book(name='O Alquimista', quantity=8, id_author=4, id_category=2),
            Book(name='Reinações de Narizinho', quantity=10, id_author=5, id_category=3),
            Book(name='Vidas Secas', quantity=7, id_author=7, id_category=1),
            Book(name='Sentimento do Mundo', quantity=5, id_author=6, id_category=4),
            Book(name='O Primo Basílio', quantity=4, id_author=8, id_category=1),
            Book(name='O Alienista', quantity=6, id_author=1, id_category=6)
        ]
        for livro in livros:
            db.session.add(livro)
        db.session.commit()

        # Criar Clientes
        clientes = [
            Client(name='João Silva', email='joao@email.com', phone='11999999999'),
            Client(name='Maria Santos', email='maria@email.com', phone='11988888888'),
            Client(name='Pedro Oliveira', email='pedro@email.com', phone='11977777777'),
            Client(name='Ana Costa', email='ana@email.com', phone='11966666666'),
            Client(name='Carlos Pereira', email='carlos@email.com', phone='11955555555')
        ]
        for cliente in clientes:
            db.session.add(cliente)
        db.session.commit()

        # Criar Empréstimos
        data_atual = datetime.now()
        data_prevista = data_atual + timedelta(days=7)
        
        # Empréstimo 1
        emprestimo1 = Loan(id_client=1, start=data_atual, expected_end=data_prevista)
        db.session.add(emprestimo1)
        db.session.commit()
        
        book_loan1 = BookLoan(id_book=1, id_loan=emprestimo1.id, book_quantity=1)
        db.session.add(book_loan1)
        
        # Empréstimo 2
        emprestimo2 = Loan(id_client=2, start=data_atual, expected_end=data_prevista)
        db.session.add(emprestimo2)
        db.session.commit()
        
        book_loan2 = BookLoan(id_book=3, id_loan=emprestimo2.id, book_quantity=1)
        db.session.add(book_loan2)
        
        # Empréstimo 3
        emprestimo3 = Loan(id_client=3, start=data_atual, expected_end=data_prevista)
        db.session.add(emprestimo3)
        db.session.commit()
        
        book_loan3 = BookLoan(id_book=5, id_loan=emprestimo3.id, book_quantity=1)
        db.session.add(book_loan3)
        
        # Empréstimo 4
        emprestimo4 = Loan(id_client=4, start=data_atual, expected_end=data_prevista)
        db.session.add(emprestimo4)
        db.session.commit()
        
        book_loan4 = BookLoan(id_book=7, id_loan=emprestimo4.id, book_quantity=1)
        db.session.add(book_loan4)
        
        db.session.commit()
        print("Banco de dados populado com sucesso!")

if __name__ == '__main__':
    populate_database() 