import click
import importlib
import os
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

from config import DATABASE_URL
#from infrastructure.bootstrap import bootstrap
#from domain.location import Location

db = SQLAlchemy()


def migrate(app):
    db_url = DATABASE_URL
    app.config.from_mapping(SQLALCHEMY_DATABASE_URI=db_url,
                            SQLALCHEMY_TRACK_MODIFICATIONS=False)
    import_models()
    db.init_app(app)
    # location = Location(longitude=10, latitude=15,
    #                    city='salvador', state='bahia', address='qlqr coisa')

    query = text(
        'insert into location (city, state, address, longitude, latitude) values ("salvador","bahia","qlqr","40","30")')
    result = db.engine.execute(query)
    print(result)
    db.add(location)
    db.commit()

    Migrate(app, db)
    return app


def import_models():
    for dir_path, dir_names, file_names in os.walk('infrastructure/mapper'):
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


@click.command("bootstrap")
@with_appcontext
def bootstrap_db_command():
    bootstrap(db)
    click.echo("Database bootstrapped")
