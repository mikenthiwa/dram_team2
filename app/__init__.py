# app/__init__.py

# third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# local imports
from instance.config import app_config

# variable initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)
    login_manager.init_app(app=app)
    login_manager.login_message = "You must be logged in to view this page"
    login_manager.login_view = "auth.login"

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
