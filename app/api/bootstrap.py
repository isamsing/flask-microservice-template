import logging

from flask import Flask
from flask_restplus import Api

from .endpoints.exampleone import example_one_name_space
from .endpoints.exampletwo import example_two_name_space

logger = logging.getLogger(__name__)


def init(configuration):
    logging.info("Application running with {} configurations".format(configuration.__class__.__name__))
    api = Api(Flask(configuration.NAME))
    api.add_namespace(example_one_name_space)
    api.add_namespace(example_two_name_space)

    api.app.config.from_object(configuration)
    return api
