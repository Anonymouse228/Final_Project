from flask import Flask
from config import Configuration, Tut, RussiaToday, Onliner, iXBT
import random

app = Flask(__name__)
app.config.from_object(Configuration)

all = []
block = []
sites = [Tut(), RussiaToday(), Onliner(), iXBT()]
max_len = 0

for i in sites:
    i.get_news()
    if len(i.href) > max_len:
        max_len = len(i.href)
for i in range(max_len):
    for j in sites:
        if i >= len(j.href):
            continue
        data = {'name': j.name,
                'link': j.href[i],
                'header': j.title[i],
                'text': j.text[i]}
        block.append(data)
    random.shuffle(block)
    for j in block:
        all.append(j)
    block = []
