from flask import Flask

from .apis.example.endpoint import example_blueprint
from .config import app_config

__all__ = ['apis', 'config', 'run.py', 'init']


def init(config_name):
    app = Flask(__name__)
    app.register_blueprint(example_blueprint)
    app.config.from_object(app_config[config_name])
    return app
