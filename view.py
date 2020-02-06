from app import app, all_news
from flask import render_template, request, json
from config import categories

section = []

for i in categories:
    section_news = []
    for j in all_news:
        if j['section'] == i[1]:
            section_news.append(j)
    section.append(section_news)


@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        return json.dumps(request.json)


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
    return render_template('index.html', all=section[0], categories=categories)


@app.route('/opinion')
def opinion():
    return render_template('index.html', all=section[1], categories=categories)


@app.route('/auto')
def auto():
    return render_template('index.html', all=section[2], categories=categories)


@app.route('/tech')
def tech():
    return render_template('index.html', all=section[3], categories=categories)


@app.route('/realty')
def realty():
    return render_template('index.html', all=section[4], categories=categories)
