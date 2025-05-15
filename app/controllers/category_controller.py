from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.category_service import CategoryService
from app.utils.exceptions import BusinessRuleError, NotFoundError

category_bp = Blueprint('category_controller', __name__)

@category_bp.route('/')
def index():
    categories = CategoryService.get_all_categories()
    return render_template('categories/index.html', categories=categories)

@category_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            CategoryService.create_category(request.form)
            flash('Categoria criada com sucesso!', 'success')
            return redirect(url_for('category_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'danger')
    return render_template('categories/form.html', category=None)

@category_bp.route('/<int:id>')
def show(id):
    try:
        category = CategoryService.get_category(id)
        return render_template('categories/show.html', category=category)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('category_controller.index'))

@category_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        category = CategoryService.get_category(id)
        if request.method == 'POST':
            try:
                CategoryService.update_category(id, request.form)
                flash('Categoria atualizada!', 'success')
                return redirect(url_for('category_controller.index'))
            except BusinessRuleError as e:
                flash(str(e), 'danger')
        return render_template('categories/form.html', category=category)
    except NotFoundError as e:
        flash(str(e), 'danger')
        return redirect(url_for('category_controller.index'))

@category_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    try:
        from app.repositories.category_repository import CategoryRepository
        CategoryRepository.delete(id)
        flash('Categoria removida com sucesso!', 'success')
    except NotFoundError as e:
        flash(str(e), 'danger')
    except BusinessRuleError as e:
        flash(str(e), 'danger')
    return redirect(url_for('category_controller.index'))