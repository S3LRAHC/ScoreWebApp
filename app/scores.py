from flask import (
    Blueprint, 
    render_template,
    redirect,
    request,
    url_for
)

from app.database import get_db

bp = Blueprint("scores", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            db.execute("""INSERT INTO user_scores (
                            user, song, difficulty, perfect, great, good, bad, miss, max_combo, grade, plate, score
                        ) VALUES (
                            'PlayerName',
                            'SongTitle',
                            'Hard',
                            100,
                            50,
                            20,
                            5,
                            2,
                            150,
                            'S',
                            'Gold',
                            95000
                        );""")
            db.commit()
            return redirect(url_for("scores.scores"))
        
    return render_template("pages/create.html")

@bp.route("/scores")
def scores():
    db = get_db()
    scores = db.execute(
        "SELECT * FROM user_scores ORDER BY created DESC"
    ).fetchall()
    return render_template("pages/scores.html", scores=scores)