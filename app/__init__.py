import os
from dotenv import load_dotenv
from flask import Flask

from app import home_page, scores, database, users

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(home_page.bp)
    app.register_blueprint(scores.bp)
    users.create_db()
    
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app