"""Mqtthandler config."""
import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
load_dotenv(os.path.join(BASE_DIR, '.env'))

class Config:
    """Mqtthandler configuration variables."""

    TESTING = False
    OFFLINE = os.environ.get('OFFLINE', '')
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
    """ use development database server"""
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


class OfflineConfig(Config):
    """ use offline database server """
    MQTT_SERVER = 'localhost'
    MQTT_PORT = 1883


class TestingConfig(Config):
    """ TBD: Testing config """
    pass


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
