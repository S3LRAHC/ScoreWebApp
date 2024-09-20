import os
from dotenv import load_dotenv
from flask import Flask

from app import database
from app.extensions import user_db as db, bcrypt, login_manager


def register_blueprints(app):
    from app import home_page, scores, pictures, users, auth
    app.register_blueprint(home_page.bp)
    app.register_blueprint(scores.bp)
    app.register_blueprint(pictures.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(auth.bp)

def create_app():
    
    app = Flask(__name__)
    # Load environment variables from a .env file
    load_dotenv()
    # Set the SQLALCHEMY_DATABASE_URI to an SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    
    app.config.from_prefixed_env()
  
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.signin'

    # Register the blueprints
    register_blueprints(app)

    # Initialize the databases
    database.init_app(app)
    # users.create_db()
    
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app