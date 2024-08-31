from flask import Blueprint, render_template

bp = Blueprint('pictures', __name__)

@bp.route('/pictures')
def pictures():
    return render_template('pages/pictures.html')
