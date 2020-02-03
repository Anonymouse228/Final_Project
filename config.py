import requests
from bs4 import BeautifulSoup as BS

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


class Configuration(object):
    DEBUG = True


class Tut():
    name = 'tut.by'

    url = 'https://news.tut.by/daynews/'

    session = requests.Session()
    connect = session.get(url, headers=headers)
    html = BS(connect.content, 'html.parser')

    def __init__(self):
        self.title = []
        self.href = []
        self.text = []
        self.string = ['', 'i', 'v', 'p']

    def get_news(self):
        for i in self.string:
            for element in Tut.html.find_all('div', attrs={'class': 'news-entry big annoticed time ni' + i}):
                self.title.append(element.find('span', attrs={'class': 'entry-head _title'}).text.replace('\xa0', ' '))
                self.href.append(element.find('a', attrs={'class': 'entry__link'})['href'])
                self.text.append(element.find('span', attrs={'class': 'entry-note'}).text.replace('\xa0', ' '))


class RussiaToday():
    name = 'russian.rt.com'

    url = 'https://russian.rt.com/news'

    session = requests.Session()
    connect = session.get(url, headers=headers)
    html = BS(connect.content, 'html.parser')

    def __init__(self):
        self.title = []
        self.href = []
        self.text = []

    def get_news(self):
        for element in RussiaToday.html.find_all('li', attrs={'class': 'listing__column listing__column_all-news listing__column_js'}):
            for i in element.find_all('div', attrs={'class': 'card__heading card__heading_all-news'}):
                self.title.append(' '.join(i.find('a', attrs={'class': 'link link_color'}).text.split()))
                self.href.append(RussiaToday.url[:22] + i.find('a', attrs={'class': 'link link_color'})['href'])
            for i in element.find_all('div', attrs={'class': 'card__summary card__summary_all-news'}):
                self.text.append(' '.join(i.find('a', attrs={'class': 'link link_color'}).text.split()))


'''class CNN():
    name = 'cnn.com'  Это гейство не работает, я больше так не могу! я потратил на это столько же времени,
                      как и на остальные 4 класса!!! Но оно не работает!!!!!! Ненавижу cnn.
                      
    url = 'https://edition.cnn.com/world'

    session = requests.Session()
    connect = session.get(url, headers=headers)
    html = BS(connect.content, 'html.parser')

    def __init__(self):
        self.text = ''
        count = 0
        for i in range(6):
            for element in CNN.html.find_all('div', attrs={'class': 'column zn__column--idx-' + str(i)}):
                self.title = element.find('span', attrs={'class': 'cd__headline-text'}).text
                if 'http' in element.find('a')['href']:
                    self.href = element.find('a')['href']
                else:
                    self.href = 'https://edition.cnn.com' + element.find('a')['href']
                for j in element.find_all('li'):
                    if j.find('span', attrs={'class': 'cd__headline-text'}):
                        self.text = self.text + j.find('span', attrs={'class': 'cd__headline-text'}).text + ' '
                print(self.title)
                print(self.href)
                print(self.text)
                print()
                self.text = ''
                count += 1
                if count % 6 > 4:
                    break'''


class Onliner():
    name = 'Onliner.by'

    url = 'https://people.onliner.by'

    session = requests.Session()
    connect = session.get(url, headers=headers)
    html = BS(connect.content, 'html.parser')

    def __init__(self):
        self.title = []
        self.href = []
        self.text = []

    def get_news(self):
        for element in Onliner.html.find_all('div', attrs={'class': 'news-tidings__item news-tidings__item_1of3 news-tidings__item_condensed'}):
            self.title.append(' '.join(element.find('span', attrs={'class': 'news-helpers_hide_mobile-small'}).text.split()))
            self.href.append(Onliner.url + element.find('a', attrs={'class': 'news-tidings__link'})['href'])
            self.text.append(' '.join(element.find('div', attrs={'class': 'news-tidings__speech news-helpers_hide_mobile-small'}).text.split()))


class iXBT():
    name = 'ixbt.com'

    url = 'https://www.ixbt.com/news/?show=tape'

    session = requests.Session()
    connect = session.get(url, headers=headers)
    html = BS(connect.content, 'html.parser')

    def __init__(self):
        self.title = []
        self.href = []
        self.text = []

    def get_news(self):
        for element in iXBT.html.find_all('div', attrs={'class': 'item no-padding'}):
            self.title.append(element.find('a', attrs={'id': ''}).text)
            self.href.append(iXBT.url[:20] + element.find('a', attrs={'id': ''})['href'])
            self.text.append(element.find('h4').text)
