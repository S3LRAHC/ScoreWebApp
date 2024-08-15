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

@bp.route("/scores")
def scores():
    return render_template("pages/scores.html")

@bp.route('/get_songs')
def get_songs():
    search = request.args.get('q', '').lower()
    songs = []
    csv_path = os.path.join(bp.root_path, 'static', 'songlist', 'arcade.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row if it exists
            for row in csv_reader:
                if len(row) > 1 and search in row[1].lower():
                    songs.append({'id': row[1], 'text': row[1]})
    except UnicodeDecodeError:
        # If UTF-8 fails, try another common encoding
        with open(csv_path, 'r', encoding='iso-8859-1') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row if it exists
            for row in csv_reader:
                if len(row) > 1 and search in row[1].lower():
                    songs.append({'id': row[1], 'text': row[1]})
    return jsonify(songs)