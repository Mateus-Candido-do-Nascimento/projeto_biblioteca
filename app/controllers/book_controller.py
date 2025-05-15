from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import BookService, AuthorService, CategoryService
from app.utils.exceptions import BusinessRuleError, NotFoundError


book_bp = Blueprint('book_controller', __name__)

@book_bp.route('/')
def index():
    books = BookService.get_all_books()
    return render_template('books/index.html', books=books)

@book_bp.route('/create', methods=['GET', 'POST'])
def create():
    authors = AuthorService.get_all_authors()
    categories = CategoryService.get_all_categories()
    
    if request.method == 'POST':
        try:
            BookService.create_book(request.form)
            flash('Livro cadastrado com sucesso!', 'success')
            return redirect(url_for('book_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'danger')
    
    return render_template('books/form.html', book=None, authors=authors, categories=categories)

@book_bp.route('/<int:id>')
def show(id):
    try:
        book = BookService.get_book_by_id(id)
        return render_template('books/show.html', book=book)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('book_controller.index'))

@book_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        book = BookService.get_book_by_id(id)
        authors = AuthorService.get_all_authors()
        categories = CategoryService.get_all_categories()
        
        if request.method == 'POST':
            try:
                BookService.update_book(id, request.form)
                flash('Livro atualizado com sucesso!', 'success')
                return redirect(url_for('book_controller.index'))
            except BusinessRuleError as e:
                flash(str(e), 'danger')
        
        return render_template('books/form.html', book=book, authors=authors, categories=categories)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('book_controller.index'))

@book_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    try:
        BookService.delete_book(id)
        flash('Livro removido com sucesso!', 'success')
    except NotFoundError as e:
        flash(str(e), 'danger')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    return redirect(url_for('book_controller.index'))

@book_bp.route('/<int:id>/return', methods=['POST'])
def return_book(id):
    try:
        BookService.return_book(id)
        flash('Livro devolvido com sucesso!', 'success')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    except NotFoundError as e:
        flash(str(e), 'danger')
    return redirect(url_for('book_controller.show', id=id))