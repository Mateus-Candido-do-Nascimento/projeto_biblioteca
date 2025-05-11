from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.category_service import CategoryService
from app.utils.exceptions import BusinessRuleError, NotFoundError

category_bp = Blueprint('category_controller', __name__)

@category_bp.route('/categories')
def index():
    categories = CategoryService.get_all_categories()
    return render_template('categories/index.html', categories=categories)

@category_bp.route('/categories/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            CategoryService.create_category(request.form)
            flash('Categoria criada com sucesso!', 'success')
            return redirect(url_for('category_controller.index'))
        except BusinessRuleError as e:
            flash(str(e), 'error')
    return render_template('categories/create.html')

@category_bp.route('/categories/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    try:
        category = CategoryService.get_category(id)
        if request.method == 'POST':
            CategoryService.update_category(id, request.form)
            flash('Categoria atualizada!', 'success')
            return redirect(url_for('category_controller.index'))
        return render_template('categories/edit.html', category=category)
    except NotFoundError as e:
        flash(str(e), 'error')
        return redirect(url_for('category_controller.index'))