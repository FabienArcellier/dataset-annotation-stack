# pylint: disable=invalid-name
import os
import shutil
from os.path import dirname

from flask import Flask
from app.apis import api
from flask_spaproxy import SpaProxy

ROOT_DIR = os.path.realpath(os.path.join(dirname(__file__), '..'))


def _init_dotenv():
    if not os.path.isfile(os.path.join(ROOT_DIR, '.env')):
        shutil.copy(os.path.join(ROOT_DIR, '.env.sample'), os.path.join(ROOT_DIR, '.env'))


_init_dotenv()
spa_proxy_url = os.getenv('FLASK_SPA_PROXY_URL', None)
static_folder = '../../frontend/build' if spa_proxy_url is None else spa_proxy_url
app = Flask(__name__, static_folder=static_folder)
SpaProxy(app)

api.init_app(app)



if __name__ == "__main__":
    app.run()
