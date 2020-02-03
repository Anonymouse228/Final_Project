from app import app, all
from flask import render_template


@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', n=name, all=all)
