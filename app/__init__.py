from flask import Flask
from flask_static_digest import FlaskStaticDigest

flask_static_digest = FlaskStaticDigest()

from app import routes
from infrastructure import migrate



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app = migrate(app)

    flask_static_digest.init_app(app)

    app.register_blueprint(routes.bp)
    return app
