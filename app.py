from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/index")
def home_page():
    return render_template('indexNew.html')

@app.route("/test")
def test():
    return render_template('layout.html')

@app.route("/testing")
def testing():
    return render_template('index.html')
