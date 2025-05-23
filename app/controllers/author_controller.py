from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.author_service import AuthorService
from app.utils.exceptions import BusinessRuleError, NotFoundError

author_bp = Blueprint('author_controller', __name__)

@author_bp.route('/')
def index():
    authors = AuthorService.get_all_authors()
    return render_template('authors/index.html', authors=authors)

@author_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            AuthorService.create_author(request.form)
            flash('Autor cadastrado com sucesso!', 'success')
            return redirect(url_for('author_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'danger')
    return render_template('authors/form.html', author=None)

@author_bp.route('/<int:id>')
def show(id):
    try:
        author = AuthorService.get_author(id)
        return render_template('authors/show.html', author=author)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('author_controller.index'))

@author_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        author = AuthorService.get_author(id)
        if request.method == 'POST':
            try:
                AuthorService.update_author(id, request.form)
                flash('Autor atualizado!', 'success')
                return redirect(url_for('author_controller.index'))
            except BusinessRuleError as e:
                flash(str(e), 'danger')
        return render_template('authors/form.html', author=author)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('author_controller.index'))

@author_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    try:
        from app.repositories.author_repository import AuthorRepository
        AuthorRepository.delete(id)
        flash('Autor removido com sucesso!', 'success')
    except NotFoundError as e:
        flash(str(e), 'danger')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    return redirect(url_for('author_controller.index'))