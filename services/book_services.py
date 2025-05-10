from models import db, Book

class BookService:
    def get_all_books(self):
        return Book.query.all()
    
    def get_book_by_id(self, id):
        return Book.query.get_or_404(id)
    
    def create_book(self, data):
        book = Book(
            name=data['name'],
            description=data['description'],
            quantity=int(data['quantity']),
            id_author=int(data['id_author']),
            id_category=int(data['id_category'])
        )
        db.session.add(book)
        db.session.commit()
        return book
    
    def update_book(self, id, data):
        book = self.get_book_by_id(id)
        book.name = data['name']
        book.description = data['description']
        book.quantity = int(data['quantity'])
        book.id_author = int(data['id_author'])
        book.id_category = int(data['id_category'])
        db.session.commit()
        return book
    
    def delete_book(self, id):
        book = self.get_book_by_id(id)
        db.session.delete(book)
        db.session.commit()