from flask import Blueprint, render_template

from infrastructure.repository.property import get_all

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
    properties = get_all()
    print(properties)
    return render_template('index.html')
