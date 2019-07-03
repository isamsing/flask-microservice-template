import sys

from app.api.bootstrap import init

if __name__ == '__main__':
    api = init(sys.argv[1])
    api.app.run()
