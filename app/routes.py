from flask import Blueprint, render_template, send_from_directory

from infrastructure.repository.property import get_by, find
from infrastructure.repository.fixtures import bootstrap
from domain.property import Property
from flask import request

from config import ASSETS_FOLDER

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
    return render_template('home.html')


@bp.route('/match')
def match():
    rooms = request.args.get('rooms')
    value = request.args.get('value')
    garages = request.args.get('garages')
    area = request.args.get('area')
    properties = get_by(rooms, value, garages, area)

    return render_template('match.html', properties=properties)


@bp.route('/boostrap')
def up_base():
    bootstrap()
    return render_template('home.html')


@bp.route('/property/<id>')
def info_property(id):
    perc = request.args.get('perc')
    property = find(id)
    return render_template('property.html', property=property, perc=perc)


@bp.route('/survey')
def survey():
    survey = [
        {
            'category': 'name',
            'question': 'Como que eu posso te chamar?'
        },
        {
            'category': 'timesearch',
            'question': 'Quanto tempo você está procurando apartamento?'
        },
        {
            'category': 'rooms',
            'question': 'Quantas pessoas vivem com você?'
        },
        {
            'category': 'value',
            'question': 'Quanto você está disposto a pagar por um novo apê?'
        },
        {
            'category': 'distance',
            'question': 'Como você costuma se deslocar para o trabalho?'
        },
    ]
    return render_template('survey.html', survey=survey)
