"""Flask config."""
import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    """Flask configuration variables."""

    # General Config
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    DISABLE_CACHE = os.environ.get("FLASK_APP_DISABLE_CACHE", "")
    DISABLE_FORCE_HTTPS = os.environ.get("FLASK_APP_DISABLE_FORCE_HTTPS", "")

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    DEBUG = False
    TESTING = False
    DB_NAME = 'data'
    MQTT_SERVER = 'lennyspi.local'
    MQTT_PORT = 8833
    SECRET_KEY = 'key'
    ADMIN = {
        'username': os.environ.get('FLASK_APP_ADMIN', 'admin'),
        'email': os.environ.get('FLASK_APP_ADMIN_EMAIL', 'admin@admin.de'),
        'password': os.environ.get('FLASK_APP_ADMIN_PASSWORD', 'admin')
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('FLASK_APP_DATABASE_USER'),
        os.environ.get('FLASK_APP_DATABASE_PASSWORD'),
        os.environ.get('FLASK_APP_DATABASE_HOST'),
        os.environ.get('FLASK_APP_DATABASE_PORT'),
        os.environ.get('FLASK_APP_DATABASE_DATA_NAME')
    )

    SQLALCHEMY_BINDS = {
        'probe_request': 'postgresql://{}:{}@{}:{}/{}'.format(
            os.environ.get('FLASK_APP_DATABASE_USER'),
            os.environ.get('FLASK_APP_DATABASE_PASSWORD'),
            os.environ.get('FLASK_APP_DATABASE_HOST'),
            os.environ.get('FLASK_APP_DATABASE_PORT'),
            os.environ.get('FLASK_APP_DATABASE_PROBES_NAME')
        ),
        'users': 'postgresql://{}:{}@{}:{}/{}'.format(
            os.environ.get('FLASK_APP_DATABASE_USER'),
            os.environ.get('FLASK_APP_DATABASE_PASSWORD'),
            os.environ.get('FLASK_APP_DATABASE_HOST'),
            os.environ.get('FLASK_APP_DATABASE_PORT'),
            os.environ.get('FLASK_APP_DATABASE_USERS_NAME')
        ),
    }


class ProductionConfig(Config):
    """Uses production database server."""
    DEBUG = False


class DevelopmentConfig(Config):
    MQTT_SERVER = 'localhost'
    MQTT_PORT = 1883
    DEBUG = True


class OfflineConfig(Config):
    DEBUG = True
    MQTT_SERVER = 'localhost'
    MQTT_PORT = 1883
    DROP_ALL = True


class TestingConfig(Config):
    DB_NAME = 'data_testing'
    MQTT_SERVER = 'localhost'
    DEBUG = True


env = os.environ.get('HANDLER_ENV', 'DEBUG')

if env == 'production':
    config = ProductionConfig
elif env == 'development':
    config = DevelopmentConfig
elif env == 'testing':
    config = TestingConfig
elif env == 'offline':
    config = OfflineConfig
else:
    config = Config
