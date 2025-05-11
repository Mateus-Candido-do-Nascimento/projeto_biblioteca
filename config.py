import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()

class Config:
    MIGRATIONS_DIR= str(Path(__file__).parent / 'migrations')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///library.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False