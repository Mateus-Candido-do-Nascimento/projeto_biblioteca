from flask import Blueprint, render_template

index_bp = Blueprint('index_controller', __name__)

@index_bp.route('/')
def index():
    return render_template('welcome.html')
