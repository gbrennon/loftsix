from flask import Blueprint, render_template, send_from_directory

from infrastructure.repository.property import get_all

from config import ASSETS_FOLDER

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def index():
    properties = get_all()
    print(properties)
    return render_template('home.html')

@bp.route('/survey')
def survey():
    questions = [
        'Voce tem filhos?',
        'Voce é estudante?',
        'Qual sua idade?'
    ];
    return render_template('survey.html', questions=questions)
