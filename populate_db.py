from app import create_app, db
from app.models import Author, Category, Book

# Dados extraídos da planilha
LIVROS = [
    # (titulo, autor, genero, isbn, disponivel)
    ("O Grande Gatsby", "F. Scott Fitzgerald", "Romance", "978-853590", True),
    ("A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", "978-85325", True),
    ("Harry Potter", "J.K. Rowling", "Fantasia", "978-85325", True),
    ("O Alquimista", "Paulo Coelho", "Ficção científica", "978-85770", True),
    ("O Sol é para Todos", "Harper Lee", "Drama", "978-85325", True),
    ("O Código Da Vinci", "Dan Brown", "Ficção científica", "978-85359", True),
    ("Jane Eyre", "Charlotte Bronte", "Romance", "978-85325", True),
    ("Guerra e Paz", "Leo Tolstoy", "Romance", "978-85359", True),
    ("O Conto da Aia", "Margaret Atwood", "Ficção científica", "978-85510", True),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", "Romance", "978-85359", True),
    ("Orgulho e Preconceito", "Jane Austen", "Romance", "978-85359", True),
    ("1984", "George Orwell", "Ficção científica", "978-85359", True),
    ("Moby Dick", "Herman Melville", "Aventura", "978-85325", True),
    ("O Hobbit", "J.R.R. Tolkien", "Fantasia", "978-85359", True),
    ("Crime e Castigo", "Fyodor Dostoevsky", "Romance", "978-85359", True),
    # ... (adicione todos os outros livros da lista aqui, seguindo o mesmo padrão)
]

def main():
    app = create_app()
    with app.app_context():
        # 1. Adicionar categorias únicas
        categorias = set(livro[2] for livro in LIVROS)
        categoria_objs = {}
        for nome in categorias:
            cat = Category.query.filter_by(name=nome).first()
            if not cat:
                cat = Category(name=nome)
                db.session.add(cat)
            categoria_objs[nome] = cat
        db.session.commit()

        # 2. Adicionar autores únicos
        autores = set(livro[1] for livro in LIVROS)
        autor_objs = {}
        for nome in autores:
            autor = Author.query.filter_by(name=nome).first()
            if not autor:
                autor = Author(name=nome)
                db.session.add(autor)
            autor_objs[nome] = autor
        db.session.commit()

        # 3. Adicionar livros
        for titulo, autor_nome, categoria_nome, isbn, disponivel in LIVROS:
            autor = autor_objs[autor_nome]
            categoria = categoria_objs[categoria_nome]
            if not Book.query.filter_by(title=titulo, author_id=autor.id).first():
                livro = Book(
                    title=titulo,
                    author_id=autor.id,
                    category_id=categoria.id,
                    isbn=isbn,
                    is_available=disponivel
                )
                db.session.add(livro)
        db.session.commit()
        print("Base populada com sucesso!")

if __name__ == "__main__":
    main() 