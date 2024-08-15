from flask import Blueprint, render_template, request, jsonify, g
from app.score_utils import get_letter_grade_and_plate
from app.score_utils import calculate_phoenix_score
from app.database import get_db
import csv
import os

bp = Blueprint("pages", __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # This handles the score submission
        db = get_db()
        try:
            db.execute(
                """INSERT INTO user_scores 
                (user, song, difficulty, perfect, great, good, bad, miss, max_combo, grade, plate, score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    request.form['username'],
                    request.form['song'],
                    request.form['matchType'] + request.form['level'],
                    request.form['perfect'],
                    request.form['great'],
                    request.form['good'],
                    request.form['bad'],
                    request.form['miss'],
                    request.form['max_combo'],
                    request.form['grade'],
                    request.form['plate'],
                    request.form['score'].replace(',', '')  # Remove comma from score
                )
            )
            db.commit()
            return jsonify({'message': 'Score submitted successfully'})
        except db.Error as e:
            return jsonify({'error': str(e)}), 500
    return render_template("pages/home.html")


@bp.route('/calculate', methods=['POST'])
def calculate_score():
    result = {
        'PERFECT': int(request.form['perfect']),
        'GREAT': int(request.form['great']),
        'GOOD': int(request.form['good']),
        'BAD': int(request.form['bad']),
        'MISS': int(request.form['miss']),
        'MAX COMBO': int(request.form['max_combo'])
    }

    score = calculate_phoenix_score(result)
    letter_grade, plate = get_letter_grade_and_plate(score, result)

    return jsonify({
        'score': f"{score:,}",
        'grade': letter_grade,
        'plate': plate
    })
