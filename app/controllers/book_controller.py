from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import BookService, AuthorService, CategoryService
from app.utils.exceptions import BusinessRuleError, NotFoundError
from app.models import Book, Client, Loan
from app.extensions import db


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

@book_bp.route('/<int:id>/loan', methods=['POST'])
def loan_book(id):
    book = Book.query.get_or_404(id)
    if not book.is_available or book.quantity <= 0:
        flash('Livro não está disponível para empréstimo.', 'danger')
        return redirect(url_for('book_controller.show', id=id))
    client_id = request.form.get('client_id')
    if not client_id:
        flash('Cliente não selecionado.', 'danger')
        return redirect(url_for('book_controller.show', id=id))
    client = Client.query.get_or_404(client_id)
    loan = Loan(book_id=book.id, client_id=client.id)
    book.quantity -= 1
    db.session.add(loan)
    db.session.commit()
    flash('Livro emprestado com sucesso!', 'success')
    return redirect(url_for('book_controller.show', id=id))