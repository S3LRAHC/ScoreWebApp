from flask import (
    Blueprint, 
    render_template,
    redirect,
    request,
    url_for
)

import math

from app.database import get_db

bp = Blueprint("scores", __name__)


@bp.route("/scores")
def scores():
    db = get_db()
    cursor = db.cursor()
    
    # Get total number of rows
    cursor.execute("SELECT COUNT(*) FROM user_scores")
    total_rows = cursor.fetchone()[0]
    
    # Calculate total pages
    rows_per_page = 5
    total_pages = math.ceil(total_rows / rows_per_page)
    
    # Get current page from query parameters, default to 1
    page = request.args.get('page', 1, type=int)
    
    # Calculate offset
    offset = (page - 1) * rows_per_page
    
    # Fetch scores for the current page
    cursor.execute("""
        SELECT *, datetime(created, 'localtime') as local_created 
        FROM user_scores 
        ORDER BY created DESC 
        LIMIT ? OFFSET ?
    """, (rows_per_page, offset))
    scores = cursor.fetchall()
    
    return render_template('pages/scores.html', scores=scores, page=page, total_pages=total_pages)