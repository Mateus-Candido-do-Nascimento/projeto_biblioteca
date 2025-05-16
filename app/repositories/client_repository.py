from app.repositories.database import db, BaseRepository
from app.models.entities.client import Client
from sqlalchemy.exc import SQLAlchemyError

class ClientRepository(BaseRepository):
    @staticmethod
    def get_all():
        return Client.query.order_by(Client.name).all()

    @staticmethod
    def get_by_id(client_id):
        return Client.query.get(client_id)

    @staticmethod
    def get_by_email(email):
        return Client.query.filter_by(email=email).first()

    @staticmethod
    def search(query):
        return Client.query.filter(
            Client.name.ilike(f'%{query}%') | 
            Client.email.ilike(f'%{query}%')
        ).all()

    @staticmethod
    def create(client_data):
        try:
            client = Client(**client_data)
            return BaseRepository.save(client)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def update(client, data):
        try:
            for key, value in data.items():
                setattr(client, key, value)
            return BaseRepository.save(client)
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e

    @staticmethod
    def delete(client):
        try:
            db.session.delete(client)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            BaseRepository.rollback()
            raise e