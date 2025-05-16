from app.models.entities import Author, Book, Category, Client, Loan

def test_author_creation():
    author = Author(name='Machado de Assis')
    assert author.name == 'Machado de Assis'

def test_category_creation():
    category = Category(name='Romance')
    assert category.name == 'Romance'

def test_client_creation():
    client = Client(name='João', email='joao@email.com', phone='123456')
    assert client.name == 'João'
    assert client.email == 'joao@email.com'
    assert client.phone == '123456'

def test_book_creation():
    book = Book(name='Dom Casmurro', quantity=3, id_author=1, id_category=1)
    assert book.name == 'Dom Casmurro'
    assert book.quantity == 3
    assert book.id_author == 1
    assert book.id_category == 1

def test_loan_creation():
    loan = Loan(id_client=1)
    assert loan.id_client == 1 