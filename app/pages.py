from flask import Blueprint, render_template, request, jsonify
from app.score_utils import get_letter_grade_and_plate
from app.score_utils import calculate_phoenix_score
import csv
import os

bp = Blueprint("pages", __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        result = {
            'PERFECT': request.form['perfect'],
            'GREAT': request.form['great'],
            'GOOD': request.form['good'],
            'BAD': request.form['bad'],
            'MISS': request.form['miss'],
            'MAX COMBO': request.form['max_combo']
        }

        score = calculate_phoenix_score(result)
        letter_grade, plate = get_letter_grade_and_plate(score, result)

        return jsonify({
            'score': f"{score:,}",
            'grade': letter_grade,
            'plate': plate
        })
    return render_template("pages/home.html")
