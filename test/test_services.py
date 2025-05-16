import pytest
from app.services.client_service import ClientService
from app.services.book_service import BookService
from app.repositories.database import db
from app.models.entities import Client, Book, Author, Category
from app.utils.exceptions import BusinessRuleError


def test_register_client(app):
    data = {'name': 'Maria', 'email': 'maria@email.com', 'phone': '9999'}
    client = ClientService.register_client(data)
    assert client.name == 'Maria'
    assert client.email == 'maria@email.com'


def test_register_client_duplicate_email(app):
    data = {'name': 'Pedro', 'email': 'pedro@email.com', 'phone': '8888'}
    ClientService.register_client(data)
    with pytest.raises(BusinessRuleError):
        ClientService.register_client(data)


def test_create_book(app):
    # Precisa de autor e categoria
    author = Author(name='Autor Teste')
    category = Category(name='Categoria Teste')
    db.session.add(author)
    db.session.add(category)
    db.session.commit()
    data = {
        'name': 'Livro Teste',
        'quantity': 5,
        'id_author': author.id,
        'id_category': category.id
    }
    book = BookService.create_book(data)
    assert book.name == 'Livro Teste'
    assert book.quantity == 5 