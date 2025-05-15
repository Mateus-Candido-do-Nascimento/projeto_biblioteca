from app.repositories import CategoryRepository
from app.models.schemas import CategorySchema
from app.utils.exceptions import NotFoundError

class CategoryService:
    @staticmethod
    def create_category(data):
        validated_data = CategorySchema().load(data)
        return CategoryRepository.create(validated_data)

    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_all()

    @staticmethod
    def get_category(category_id):
        if category := CategoryRepository.get_by_id(category_id):
            return category
        raise NotFoundError("Categoria não encontrada")

    @staticmethod
    def update_category(category_id, data):
        validated_data = CategorySchema().load(data, partial=True)
        if category := CategoryRepository.update(category_id, validated_data):
            return category
        raise NotFoundError("Categoria não encontrada")