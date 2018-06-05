# app/__init__.py

# third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from instance.config import app_config

# variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
