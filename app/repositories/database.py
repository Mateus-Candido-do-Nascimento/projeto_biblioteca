from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(
    session_options={
        'autoflush': False,
        'autocommit': False
    }
)

class BaseRepository:
    @staticmethod
    def save(entity):
        db.session.add(entity)
        try:
            db.session.commit()
            return entity
        except:
            db.session.rollback()
            raise

    @staticmethod
    def rollback():
        db.session.rollback()