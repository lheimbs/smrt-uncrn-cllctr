"""Mqtthandler config."""
import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, '.env'))

env = os.environ.get('HANDLER_ENV', 'DEBUG')

class Config:
    """Mqtthandler configuration variables."""

    DEBUG = False
    TESTING = False
    MQTT_SERVER = 'lennyspi.local'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

    SQLALCHEMY_BINDS = {
        'probe_request': 'sqlite:///data_probes.db',
        'users': 'sqlite:///data_users.db',
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Uses production database server."""
    DB_NAME = 'data_production'

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('DATABASE_USER', 'lenny'),
        os.environ.get('DATABASE_PASSWORD', ''),
        os.environ.get('DATABASE_HOST', 'dashboard.heimbs.me'),
        os.environ.get('DATABASE_PORT', 65432),
        os.environ.get('DATABASE_NAME', 'data_production')
    )

    SQLALCHEMY_BINDS = {
        'probe_request': 'postgresql://{}:{}@{}:{}/{}'.format(
            os.environ.get('DATABASE_USER', 'lenny'),
            os.environ.get('DATABASE_PASSWORD', ''),
            os.environ.get('DATABASE_HOST', 'dashboard.heimbs.me'),
            os.environ.get('DATABASE_PORT', 65432),
            os.environ.get('DATABASE_NAME', 'probes_production')
        ),
        'users': 'postgresql://{}:{}@{}:{}/{}'.format(
            os.environ.get('DATABASE_USER', 'lenny'),
            os.environ.get('DATABASE_PASSWORD', ''),
            os.environ.get('DATABASE_HOST', 'dashboard.heimbs.me'),
            os.environ.get('DATABASE_PORT', 65432),
            os.environ.get('DATABASE_NAME', 'users_production')
        ),
    }


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ.get('DATABASE_USER', 'pi'),
        os.environ.get('DATABASE_PASSWORD', ''),
        os.environ.get('DATABASE_HOST', 'lennyspi.local'),
        os.environ.get('DATABASE_PORT', 5432),
        os.environ.get('DATABASE_NAME', 'data')
    )

    SQLALCHEMY_BINDS = {
        'probe_request': 'postgresql://{}:{}@{}:{}/{}'.format(
            os.environ.get('DATABASE_USER', 'pi'),
            os.environ.get('DATABASE_PASSWORD', ''),
            os.environ.get('DATABASE_HOST', 'lennyspi.local'),
            os.environ.get('DATABASE_PORT', 5432),
            os.environ.get('DATABASE_NAME', 'probes')
        ),
        'users': 'postgresql://{}:{}@{}:{}/{}'.format(
            os.environ.get('DATABASE_USER', 'pi'),
            os.environ.get('DATABASE_PASSWORD', ''),
            os.environ.get('DATABASE_HOST', 'lennyspi.local'),
            os.environ.get('DATABASE_PORT', 5432),
            os.environ.get('DATABASE_NAME', 'users')
        ),
    }
    MQTT_SERVER = 'localhost'
    MQTT_PORT = 1883
    DEBUG = True


class OfflineConfig(Config):
    DEBUG = True
    MQTT_SERVER = 'localhost'
    MQTT_PORT = 1883
    DROP_ALL = True


class TestingConfig(Config):
    MQTT_SERVER = 'localhost'
    DEBUG = True


if env == 'production':
    config = ProductionConfig
elif env == 'development':
    config = DevelopmentConfig
elif env == 'testing':
    config = TestingConfig
elif env == 'offline':
    config = OfflineConfig
else:
    config = DevelopmentConfig
