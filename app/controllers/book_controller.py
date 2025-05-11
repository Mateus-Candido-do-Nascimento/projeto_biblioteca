from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import BookService, AuthorService, CategoryService
from app.utils.exceptions import BusinessRuleError, NotFoundError

book_bp = Blueprint('book_controller', __name__)

@book_bp.route('/books')
def index():
    books = BookService.get_all_books()
    return render_template('books/index.html', books=books)

@book_bp.route('/books/create', methods=['GET', 'POST'])
def create():
    authors = AuthorService.get_all_authors()
    categories = CategoryService.get_all_categories()
    
    if request.method == 'POST':
        try:
            BookService.create_book(request.form)
            flash('Livro cadastrado com sucesso!', 'success')
            return redirect(url_for('book_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'error')
    
    return render_template('books/create.html', authors=authors, categories=categories)

@book_bp.route('/books/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        book = BookService.get_book_by_id(id)
        authors = AuthorService.get_all_authors()
        categories = CategoryService.get_all_categories()
        
        if request.method == 'POST':
            BookService.update_book(id, request.form)
            flash('Livro atualizado!', 'success')
            return redirect(url_for('book_controller.index'))
        
        return render_template('books/edit.html', book=book, authors=authors, categories=categories)
    except NotFoundError as e:
        flash(str(e), 'error')
        return redirect(url_for('book_controller.index'))