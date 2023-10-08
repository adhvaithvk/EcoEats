from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/index")
def home_page():
    return render_template('index.html')

@app.route("/journey")
def journey():
    return render_template('journey.html')
