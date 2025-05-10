from app.repositories.database import db, BaseRepository
from app.models.entities.category import Category
from sqlalchemy.exc import SQLAlchemyError

class CategoryRepository(BaseRepository):
    @staticmethod
    def get_all():
        """Retorna todas as categorias ordenadas por nome"""
        return Category.query.order_by(Category.name).all()

    @staticmethod
    def get_by_id(category_id):
        """Busca uma categoria por ID"""
        return Category.query.get(category_id)

    @staticmethod
    def get_by_name(name):
        """Busca categorias por nome (case-insensitive, busca parcial)"""
        return Category.query.filter(Category.name.ilike(f'%{name}%')).all()

    @staticmethod
    def create(category_data):
        """
        Cria uma nova categoria
        Args:
            category_data: Dicionário com {name: string}
        Returns:
            Category: Objeto criado
        Raises:
            SQLAlchemyError: Em caso de erro no banco
        """
        try:
            category = Category(**category_data)
            return BaseRepository.save(category)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def update(category_id, category_data):
        """
        Atualiza uma categoria existente
        Args:
            category_id: ID da categoria
            category_data: Dicionário com campos para atualizar
        Returns:
            Category: Objeto atualizado ou None se não encontrado
        """
        category = CategoryRepository.get_by_id(category_id)
        if not category:
            return None
            
        try:
            for key, value in category_data.items():
                setattr(category, key, value)
            return BaseRepository.save(category)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def delete(category_id):
        """
        Remove uma categoria
        Args:
            category_id: ID da categoria
        Returns:
            bool: True se removido, False se não encontrado
        """
        category = CategoryRepository.get_by_id(category_id)
        if not category:
            return False
            
        try:
            db.session.delete(category)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e