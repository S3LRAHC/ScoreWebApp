import bcrypt
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import  UserMixin, login_user, login_required, logout_user, current_user
from app import db, bcrypt, login_manager


bp = Blueprint('auth', __name__)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Function to create the database
def create_db():
    db.create_all()  # This creates all tables for models defined in this module

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    from app import db, bcrypt

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if username or email already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists', 'danger')
            return redirect(url_for('auth.signup'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.signin'))

    return render_template('pages/signup.html')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('You have been logged in!', 'success')
            
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('auth.dashboard'))

        flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('pages/signin.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/dashboard.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.signin'))
