from flask import Flask
from app import routes

from infrastructure import migrate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app = migrate(app)
    app.register_blueprint(routes.bp)
    return app
