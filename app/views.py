from app import app
from flask import Flask, render_template

@app.route("/")
def index():
    return 'Hello World'

@app.route('/about')
def about():
    # return "<h1 style='color:red'> ABOUT </h1>"
    return render_template("index.html")