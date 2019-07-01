import logging

from flask import Flask

from .api.endpoints.example import example_api
from .configuration import configurations

logger = logging.getLogger(__name__)


def init(config):
    app = Flask(__name__)
    app.register_blueprint(example_api.blueprint)
    logging.info("Application running with {} configurations".format(config))
    app.config.from_object(configurations[config])
    return app
