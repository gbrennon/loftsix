from flask import Blueprint, render_template, send_from_directory

from infrastructure.repository.property import get_by
from infrastructure.repository.fixtures import bootstrap
from domain.property import Property
from flask import request

from config import ASSETS_FOLDER

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
<<<<<<< HEAD
    return render_template('home.html')


@bp.route('/match')
def match():
    rooms = request.args.get('rooms')
    value = request.args.get('value')
    garages = request.args.get('garages')
    area = request.args.get('area')
    properties = get_by(rooms, value, garages, area)
    print(rooms, properties)

    return render_template('match.html', properties=properties)


@bp.route('/boostrap')
def up_base():
    bootstrap()
=======
    properties = get_all()
    print(properties)
    return render_template('home.html')

@bp.route('/survey')
def survey():
    return render_template('survey.html')
>>>>>>> 390d626a1027b149b3433a5b1ff6d008afa2a47e
