from flask import Flask

#packages
from app import pages
from app import database

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    
    engine, Base = database.create_db()
    
    return app