from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Book, Author, Category
from services.book_service import BookService

book_bp = Blueprint('books', __name__, url_prefix='/books')
book_service = BookService()

@book_bp.route('/')
def index():
    books = book_service.get_all_books()
    return render_template('books/list.html', books=books)

@book_bp.route('/<int:id>')
def show(id):
    book = book_service.get_book_by_id(id)
    return render_template('books/show.html', book=book)

@book_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form.to_dict()
        book_service.create_book(data)
        flash('Livro criado com sucesso!', 'success')
        return redirect(url_for('books.index'))
    
    authors = Author.query.all()
    categories = Category.query.all()
    return render_template('books/create.html', authors=authors, categories=categories)

@book_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    book = book_service.get_book_by_id(id)
    
    if request.method == 'POST':
        data = request.form.to_dict()
        book_service.update_book(id, data)
        flash('Livro atualizado com sucesso!', 'success')
        return redirect(url_for('books.show', id=id))
    
    authors = Author.query.all()
    categories = Category.query.all()
    return render_template('books/edit.html', book=book, authors=authors, categories=categories)

@book_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    book_service.delete_book(id)
    flash('Livro deletado com sucesso!', 'success')
    return redirect(url_for('books.index'))