"""Flask config."""
import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


class Config:
    """Flask configuration variables."""
    DEBUG = False
    TESTING = False

    MQTT_SERVER = os.environ.get('MQTT_SERVER', 'lennyspi.local')
    MQTT_PORT = os.environ.get('MQTT_PORT', 8833)

    OFFLINE = os.environ.get('HANDLER_OFFLINE', '')

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
