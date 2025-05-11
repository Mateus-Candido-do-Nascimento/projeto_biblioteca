from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.author_service import AuthorService
from app.utils.exceptions import BusinessRuleError, NotFoundError

author_bp = Blueprint('author_controller', __name__)

@author_bp.route('/authors', methods=['GET'])
def index():
    authors = AuthorService.get_all_authors()
    return render_template('authors/index.html', authors=authors)

@author_bp.route('/authors/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            AuthorService.create_author(request.form)
            flash('Autor cadastrado com sucesso!', 'success')
            return redirect(url_for('author_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'error')
    return render_template('authors/create.html')

@author_bp.route('/authors/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        author = AuthorService.get_author(id)
        if request.method == 'POST':
            AuthorService.update_author(id, request.form)
            flash('Autor atualizado!', 'success')
            return redirect(url_for('author_controller.index'))
        return render_template('authors/edit.html', author=author)
    except NotFoundError as e:
        flash(str(e), 'error')
        return redirect(url_for('author_controller.index'))