import logging

from flask import Flask
from flask_restplus import Api

from .endpoints.exampleone import example_one_name_space
from .endpoints.exampletwo import example_two_name_space
from .configuration import configurations

logger = logging.getLogger(__name__)


def init(config):
    api = Api(Flask(__name__))
    api.add_namespace(example_one_name_space)
    api.add_namespace(example_two_name_space)
    logging.info("Application running with {} configurations".format(config))
    api.app.config.from_object(configurations[config])
    return api
