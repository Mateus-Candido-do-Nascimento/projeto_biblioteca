from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registrar blueprints (controladores)
from controllers.book_controller import book_bp
from controllers.author_controller import author_bp
from controllers.client_controller import client_bp
from controllers.loan_controller import loan_bp
from controllers.category_controller import category_bp

app.register_blueprint(book_bp)
app.register_blueprint(author_bp)
app.register_blueprint(client_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(category_bp)

@app.route('/')
def home():
    return "Bem-vindo ao Sistema de Biblioteca"

if __name__ == '__main__':
    app.run(debug=True)