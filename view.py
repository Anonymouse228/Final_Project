from app import app, all_news
from flask import render_template, request
from config import categories


@app.route('/')
def index():
    return render_template('index.html', all=all_news, categories=categories)


@app.route('/search')
def search():
    result = []
    data = request.args['data'].lower()
    for i in all_news:
        if data in i['header'].lower() or data in i['text'].lower():
            result.append(i)
    return render_template('index.html', all=result)


@app.route('/daynews')
def daynews():
    result = []
    for i in all_news:
        if 'daynews' in i["section"]:
            result.append(i)
    return render_template('index.html', all=result, categories=categories)


@app.route('/opinion')
def opinion():
    result = []
    for i in all_news:
        if i["section"] == 'opinion':
            result.append(i)
    return render_template('index.html', all=result, categories=categories)


@app.route('/auto')
def auto():
    result = []
    for i in all_news:
        if i["section"] == 'auto':
            result.append(i)
    return render_template('index.html', all=result, categories=categories)


@app.route('/tech')
def tech():
    result = []
    for i in all_news:
        if 'tech' in i["section"]:
            result.append(i)
    return render_template('index.html', all=result, categories=categories)


@app.route('/realty')
def realty():
    result = []
    for i in all_news:
        if i["section"] == 'realt':
            result.append(i)
    return render_template('index.html', all=result, categories=categories)

