from flask import Flask, render_template, session, redirect, url_for, request, current_app, abort
from auth import auth_bp
from users import create_table

app = Flask(__name__)
app.secret_key = "14D7FD24939EEBCE"

app.register_blueprint(auth_bp, url_prefix="/auth")

with app.app_context():
    create_table()

@app.route("/")
def login():
    if session.get('logged_in'):
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login_page'))
        # return render_template('login.html')

@app.route("/index")
def home_page():
    return render_template('index.html')

@app.route("/journey")
def journey():
    return render_template('journey.html')
