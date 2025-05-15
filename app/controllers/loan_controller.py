from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import LoanService, ClientService, BookService
from app.utils.exceptions import BusinessRuleError, NotFoundError
from datetime import datetime

loan_bp = Blueprint('loan_controller', __name__)

@loan_bp.route('/')
def index():
    loans = LoanService.get_all_loans()
    return render_template('loans/index.html', loans=loans, now=datetime.utcnow())

@loan_bp.route('/create', methods=['GET', 'POST'])
def create():
    clients = ClientService.get_all_clients()
    books = BookService.get_all_books()
    selected_book_id = request.args.get('book_id', type=int)
    if request.method == 'POST':
        try:
            client_id = request.form['client_id']
            book_id = request.form['book_id']
            expected_end = request.form['end']
            # Validação: data de devolução não pode ser anterior à data atual
            if datetime.strptime(expected_end, "%Y-%m-%d").date() < datetime.utcnow().date():
                flash('A data de devolução não pode ser anterior à data atual.', 'danger')
                return render_template('loans/form.html', clients=clients, available_books=books, selected_book_id=selected_book_id)
            LoanService.create_loan(client_id, [book_id], expected_end)
            flash('Empréstimo registrado com sucesso!', 'success')
            return redirect(url_for('loan_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'danger')
        except NotFoundError as e:
            flash(str(e), 'danger')
    return render_template('loans/form.html', clients=clients, available_books=books, selected_book_id=selected_book_id)

@loan_bp.route('/<int:id>')
def show(id):
    try:
        loan = LoanService.get_loan_by_id(id)
        is_late = loan.expected_end and loan.expected_end.date() < datetime.utcnow().date()
        return render_template('loans/show.html', loan=loan, is_late=is_late, now=datetime.utcnow())
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('loan_controller.index'))

@loan_bp.route('/<int:id>/return', methods=['POST'])
def return_books(id):
    try:
        loan, is_late = LoanService.finalize_loan(id)
        if is_late:
            flash('Livros devolvidos com sucesso! (Empréstimo estava atrasado)', 'warning')
        else:
            flash('Livros devolvidos com sucesso!', 'success')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    except NotFoundError as e:
        flash(str(e), 'danger')
    return redirect(url_for('loan_controller.show', id=id))

@loan_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    try:
        LoanService.delete_loan(id)
        flash('Empréstimo removido com sucesso!', 'success')
    except NotFoundError as e:
        flash(str(e), 'danger')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    return redirect(url_for('loan_controller.index'))