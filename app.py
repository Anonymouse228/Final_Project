from flask import Flask
from config import Configuration, categories, Tut, RussiaToday, Onliner, iXBT
import random, json, datetime


def sort_col(i):
    return i['time']


app = Flask(__name__)
app.config.from_object(Configuration)


all_news = []
norm_time = []
sites = [Tut(), RussiaToday(), Onliner(), iXBT()]

for i in sites:
    i.get_news()
    all_news += i.all_news
all_news.sort(key=sort_col, reverse=True)

try:
    with open('static/articles/article_list.json', "r", encoding='utf8') as read_file:
        old_news = json.load(read_file)

    new_news = []
    for i in all_news:
        if i not in old_news:
            new_news.append(i)

    all_news = new_news + old_news

    with open('static/articles/article_list.json', "w", encoding='utf8') as f:
        json.dump(all_news, f, ensure_ascii=False)
except Exception:
    with open('static/articles/article_list.json', "w", encoding='utf8') as f:
        json.dump(all_news, f, ensure_ascii=False)

print(len(all_news))
