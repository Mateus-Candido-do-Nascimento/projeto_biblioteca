from flask.cli import FlaskGroup
from app import create_app
from app.repositories.database import db
from app.models.entities import *

app = create_app()
cli = FlaskGroup(app)  # permite rodar comandos tipo python run.py db upgrade

if __name__ == '__main__':
    cli()  # executa CLI (inclui run, db, etc.)