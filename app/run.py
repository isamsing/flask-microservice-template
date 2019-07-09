import sys

from api.bootstrap import init
from api.configuration import configurations

if __name__ == '__main__':
    configuration = configurations[sys.argv[1]]
    api = init(configuration())
    api.app.run()
