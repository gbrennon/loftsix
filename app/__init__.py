from flask import Flask
from app import routes

from infrastructure import migrate

from infrastructure import init_db_command, bootstrap_db_command


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app = migrate(app)
    app.cli.add_command(init_db_command)
    app.cli.add_command(bootstrap_db_command)

    app.register_blueprint(routes.bp)
    return app
