import sys

from app.bootstrap import init

if __name__ == '__main__':
    api = init(sys.argv[1])
    api.app.run()
