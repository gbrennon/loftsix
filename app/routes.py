from flask import Blueprint, render_template

from infrastucture.repository import property as Property

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
    properties = Property.get_all()
    return render_template('index.html')
