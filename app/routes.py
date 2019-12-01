from flask import Blueprint, render_template, send_from_directory

from infrastructure.repository.property import get_all
from infrastructure.repository.fixtures import bootstrap
from domain.property import Property

from config import ASSETS_FOLDER

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
    properties = get_all()
    print(properties)
    return render_template('index.html')


@bp.route('/boostrap')
def up_base():
    bootstrap()
