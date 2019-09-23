import logging

from api.bootstrap import init
from api.configuration import configurations

configuration = configurations["production"]
api = init(configuration())
app = api.app

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',
                port=5000,
                threaded=True,
                use_reloader=False)
    except Exception as exp:
        logging.error(exp)
