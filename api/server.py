from flask import Flask

import config
from apis.v1 import blueprint as api1

config.setup_logging()
SERVER = Flask(__name__)
SERVER.register_blueprint(api1)

if __name__ == "__main__":
    SERVER.env = config.DEV_ENV
    SERVER.run(host=config.DEV_HOST, port=config.DEV_PORT, debug=True)
