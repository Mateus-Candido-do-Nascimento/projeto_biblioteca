from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import LoanService, ClientService, BookService
from app.utils.exceptions import BusinessRuleError, NotFoundError

loan_bp = Blueprint('loan_controller', __name__)

@loan_bp.route('/loans')
def index():
    loans = LoanService.get_all_loans()
    return render_template('loans/index.html', loans=loans)

@loan_bp.route('/loans/create', methods=['GET', 'POST'])
def create():
    clients = ClientService.get_all_clients()
    books = BookService.get_all_available_books()
    
    if request.method == 'POST':
        try:
            book_ids = request.form.getlist('book_ids')
            LoanService.create_loan(request.form['id_client'], book_ids)
            flash('Empréstimo registrado!', 'success')
            return redirect(url_for('loan_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'error')
    
    return render_template('loans/create.html', clients=clients, books=books)

@loan_bp.route('/loans/<int:id>/finalize')
def finalize(id):
    try:
        LoanService.finalize_loan(id)
        flash('Empréstimo finalizado!', 'success')
    except (NotFoundError, BusinessRuleError) as e:
        flash(str(e), 'error')
    return redirect(url_for('loan_controller.index'))