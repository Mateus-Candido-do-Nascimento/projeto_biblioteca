from app.repositories import AuthorRepository
from app.models.schemas import AuthorSchema
from app.utils.exceptions import NotFoundError

class AuthorService:
    @staticmethod
    def create_author(data):
        validated_data = AuthorSchema().load(data)
        return AuthorRepository.create(validated_data)

    @staticmethod
    def get_all_authors():
        return AuthorRepository.get_all()

    @staticmethod
    def get_author(author_id):
        if author := AuthorRepository.get_by_id(author_id):
            return author
        raise NotFoundError("Autor não encontrado")

    @staticmethod
    def update_author(author_id, data):
        validated_data = AuthorSchema().load(data, partial=True)
        if author := AuthorRepository.update(author_id, validated_data):
            return author
        raise NotFoundError("Autor não encontrado")

    @staticmethod
    def search_authors(query):
        return AuthorRepository.get_by_name(query)