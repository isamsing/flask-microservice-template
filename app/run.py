import sys

from app import init

if __name__ == '__main__':
    app = init(sys.argv[1])
    app.run()
