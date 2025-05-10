from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseRepository:
    @staticmethod
    def save(entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    @staticmethod
    def rollback():
        db.session.rollback()