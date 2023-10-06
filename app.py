from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/home")
def home_page():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('layout.html')

