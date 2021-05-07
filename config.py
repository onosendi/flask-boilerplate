import os

from dotenv import load_dotenv

# Load environment variables.
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class BaseConfig:
    ''' Do not load this config directly. '''
    APP_NAME = 'Flask boilerplate'
    LOGIN_REDIRECT_ENDPOINT = 'users.index';
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']

    SESSION_COOKIE_SAMESITE = 'lax'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') \
        or 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # If set to True SQLAlchemy will log all the statements issued to stderr
    # which can be useful for debugging.
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
