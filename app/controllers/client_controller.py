from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.client_service import ClientService
from app.utils.exceptions import BusinessRuleError, NotFoundError

client_bp = Blueprint('client_controller', __name__)

@client_bp.route('/clients')
def index():
    clients = ClientService.get_all_clients()
    return render_template('clients/index.html', clients=clients)

@client_bp.route('/clients/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            ClientService.create_client(request.form)
            flash('Cliente cadastrado!', 'success')
            return redirect(url_for('client_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'error')
    return render_template('clients/create.html')

@client_bp.route('/clients/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        client = ClientService.get_client_by_id(id)
        if request.method == 'POST':
            ClientService.update_client(id, request.form)
            flash('Cliente atualizado!', 'success')
            return redirect(url_for('client_controller.index'))
        return render_template('clients/edit.html', client=client)
    except NotFoundError as e:
        flash(str(e), 'error')
        return redirect(url_for('client_controller.index'))