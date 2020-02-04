from app import app, all
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', all=all)
