from flask import Blueprint, jsonify
from extensions import db
from models.book import Book

# Cria o Blueprint para rotas de livros
book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': book.id,
        'name': book.name,
        'quantity': book.quantity
    } for book in books])

@book_bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'name': book.name,
        'description': book.description,
        'quantity': book.quantity
    })