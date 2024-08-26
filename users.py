from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # This will create the tables in the database
    print("Database tables created.")
