from flask import Blueprint, render_template, jsonify, request
from app.auth import User


bp = Blueprint('users', __name__)

@bp.route('/search_users', methods=['GET'])
def search_users():
    query = request.args.get('query')
    if not query:
        return jsonify([])  # Return an empty list if no query is provided
        
    results = User.query.filter(User.username.ilike(f'%{query}%')).all()
    serialized_results = [{'username': user.username} for user in results]

    # print(jsonify(serialized_results))

    return jsonify(serialized_results)
