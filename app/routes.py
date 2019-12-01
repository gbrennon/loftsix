from flask import Blueprint, render_template

from infrastructure.repository.property import get_all
from infrastructure.repository.fixtures import bootstrap
from domain.property import Property

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
    properties = get_all()
    print(properties)
    return render_template('index.html')


@bp.route('/boostrap')
def up_base():
    bootstrap()
