from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import ClientService
from app.utils.exceptions import BusinessRuleError, NotFoundError

client_bp = Blueprint('client_controller', __name__)

@client_bp.route('/')
def index():
    clients = ClientService.get_all_clients()
    return render_template('clients/index.html', clients=clients)

@client_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            ClientService.register_client(request.form)
            flash('Cliente cadastrado com sucesso!', 'success')
            return redirect(url_for('client_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'danger')
    return render_template('clients/form.html', client=None)

@client_bp.route('/<int:id>')
def show(id):
    try:
        client = ClientService.get_client_by_id(id)
        return render_template('clients/show.html', client=client)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('client_controller.index'))

@client_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        client = ClientService.get_client_by_id(id)
        if request.method == 'POST':
            try:
                ClientService.update_client(id, request.form)
                flash('Cliente atualizado com sucesso!', 'success')
                return redirect(url_for('client_controller.index'))
            except BusinessRuleError as e:
                flash(str(e), 'danger')
        return render_template('clients/form.html', client=client)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('client_controller.index'))

@client_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    try:
        ClientService.delete_client(id)
        flash('Cliente removido com sucesso!', 'success')
    except NotFoundError as e:
        flash(str(e), 'danger')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    return redirect(url_for('client_controller.index'))