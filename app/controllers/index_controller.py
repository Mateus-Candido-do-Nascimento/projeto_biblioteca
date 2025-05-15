from flask import Blueprint, redirect, url_for

index_bp = Blueprint('index_controller', __name__)

@index_bp.route('/')
def index():
    return redirect(url_for('book_controller.index'))
