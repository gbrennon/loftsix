import click
import importlib
import os
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

from config import DATABASE_URL

db = SQLAlchemy()


def migrate(app):
    db_url = DATABASE_URL
    app.config.from_mapping(SQLALCHEMY_DATABASE_URI=db_url,
                            SQLALCHEMY_TRACK_MODIFICATIONS=False)
    import_models()
    db.init_app(app)
    Migrate(app, db)
    app.cli.add_command(init_db_command)
    return app


def import_models():
    for dir_path, _, file_names in os.walk('infrastructure/mapper'):
        for file_name in file_names:
            if file_name.endswith("py") and file_name not in '__init__.py':
                print(file_name)
                file_path_wo_ext, _ = os.path.splitext(
                    (os.path.join(dir_path, file_name)))
                module_name = file_path_wo_ext.replace(os.sep, ".")
                importlib.import_module(module_name)


@click.command("migrations")
@with_appcontext
def init_db_command():
    import_models()
    db.create_all()
    click.echo("Initialized the database")
