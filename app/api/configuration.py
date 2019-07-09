import os


class Configuration(object):
    NAME = "FlaskRestApplication"
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    HOST = os.environ.get('FLASK_HOST', "0.0.0.0")
    PORT = os.environ.get('FLASK_PORT', "5000")
    SERVER_NAME = "{}:{}".format(HOST, PORT)


class TestConfiguration(Configuration):
    TESTING = True
    DEBUG = True


class DevelopmentConfiguration(Configuration):
    TESTING = False
    DEBUG = True


class ProductionConfiguration(Configuration):
    TESTING = False
    DEBUG = False


configurations = {
    'test': TestConfiguration,
    'development': DevelopmentConfiguration,
    'production': ProductionConfiguration,
}
