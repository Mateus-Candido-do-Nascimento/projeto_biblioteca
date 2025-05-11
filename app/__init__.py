from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.repositories.database import db
from flask_migrate import Migrate
from app.models.entities import Author, Book, Category, Client, Loan

migrate= Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.secret_key = 'dev-secret-key'  # Para flash messages
    print(app.config.get('MIGRATIONS_DIR'))  # Verifique se o caminho está correto
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar todos os blueprints
    from app.controllers.author_controller import author_bp
    from app.controllers.book_controller import book_bp
    from app.controllers.category_controller import category_bp
    from app.controllers.client_controller import client_bp
    from app.controllers.loan_controller import loan_bp

    app.register_blueprint(author_bp, url_prefix='/authors')
    app.register_blueprint(book_bp, url_prefix='/books')
    app.register_blueprint(category_bp, url_prefix='/categories')
    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(loan_bp, url_prefix='/loans')

    return app