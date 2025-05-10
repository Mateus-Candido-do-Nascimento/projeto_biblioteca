import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'segredo-super-secreto'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///biblioteca.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False