from app.repositories.author_repository import AuthorRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.client_repository import ClientRepository
from app.repositories.database import db

def test_create_and_get_author(app):
    author = AuthorRepository.create({'name': 'Autor Repo'})
    assert author.name == 'Autor Repo'
    fetched = AuthorRepository.get_by_id(author.id)
    assert fetched.name == 'Autor Repo'

def test_create_and_get_category(app):
    category = CategoryRepository.create({'name': 'Categoria Repo'})
    assert category.name == 'Categoria Repo'
    fetched = CategoryRepository.get_by_id(category.id)
    assert fetched.name == 'Categoria Repo'

def test_create_and_get_client(app):
    data = {'name': 'Cliente Repo', 'email': 'repo@email.com', 'phone': '9999'}
    client = ClientRepository.create(data)
    assert client.name == 'Cliente Repo'
    fetched = ClientRepository.get_by_id(client.id)
    assert fetched.email == 'repo@email.com' 