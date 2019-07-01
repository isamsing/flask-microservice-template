import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    HOST = os.environ.get('FLASK_HOST', "0.0.0.0")
    PORT = os.environ.get('FLASK_PORT', "5000")
    SERVER_NAME = "{}:{}".format(HOST, PORT)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
