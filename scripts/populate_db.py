from app import create_app
from app.services import AuthorService, CategoryService, BookService
from app.repositories import AuthorRepository, CategoryRepository
from app.models.entities.book import Book
from app.repositories.book_repository import BookRepository

# Lista de livros (adicione todos os livros da sua planilha aqui)
LIVROS = [
    # (titulo, autor, genero, isbn, disponivel)
    ("O Grande Gatsby", "F. Scott Fitzgerald", "Romance", "978-853590", True),
    ("A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", "978-85325", True),
    ("Harry Potter", "J.K. Rowling", "Fantasia", "978-85325", True),
    ("O Alquimista", "Paulo Coelho", "Ficção científica", "978-85770", True),
    ("O Sol é para Todos", "Harper Lee", "Drama", "978-85325", True),
    # ... (adicione todos os outros livros da lista aqui)
]

def get_or_create_category(name):
    categorias = CategoryRepository.get_by_name(name)
    for cat in categorias:
        if cat.name.lower() == name.lower():
            return cat
    return CategoryService.create_category({"name": name})

def get_or_create_author(name):
    autores = AuthorRepository.get_by_name(name)
    for autor in autores:
        if autor.name.lower() == name.lower():
            return autor
    return AuthorService.create_author({"name": name})

def main():
    app = create_app()
    with app.app_context():
        for titulo, autor_nome, categoria_nome, isbn, disponivel in LIVROS:
            categoria = get_or_create_category(categoria_nome)
            autor = get_or_create_author(autor_nome)
            # Verifica se já existe livro com mesmo nome e autor
            livros_existentes = Book.query.filter_by(name=titulo, id_author=autor.id).all()
            if livros_existentes:
                print(f"Livro '{titulo}' de '{autor_nome}' já existe. Pulando...")
                continue
            book_data = {
                "name": titulo,
                "id_author": autor.id,
                "id_category": categoria.id,
                "quantity": 1,
                "isbn": isbn,
            }
            BookService.create_book(book_data)
            print(f"Livro '{titulo}' adicionado com sucesso!")
        print("Base populada com sucesso!")

if __name__ == "__main__":
    main() 