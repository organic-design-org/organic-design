import os

from flask import Flask, session
from app.blueprints.api import api
from app.blueprints.home import home
from app.blueprints.div import div
from app.blueprints.nav import nav

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    ## Set secret key ##
    app.secret_key = os.urandom(24)
    ## Register Blueprints ##
    app.register_blueprint(home)
    app.register_blueprint(div)
    app.register_blueprint(nav)
    app.register_blueprint(api)
    return app

