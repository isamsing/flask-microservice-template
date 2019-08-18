import logging
import sys

from api.bootstrap import init
from api.configuration import configurations

configuration = configurations[sys.argv[1]]
api = init(configuration())
app = api.app

if __name__ == '__main__':
    try:
        app.run(threaded=True, use_reloader=False)
    except Exception as exp:
        logging.error(exp)
