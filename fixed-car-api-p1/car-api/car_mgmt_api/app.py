import os

import flask.cli
from car_mgmt_api.app_factory import create_app


flask.cli.load_dotenv()
app = create_app(__name__, os.environ)
