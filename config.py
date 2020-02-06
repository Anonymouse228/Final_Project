import requests, re, datetime
from bs4 import BeautifulSoup as BS
import time as tm

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
categories = [['Новость дня', 'daynews'], ['Мнения', 'opinion'], ['Авто', 'auto'], ['Технологии', 'tech'],
              ['Недвижимость', 'realty']]


class Configuration(object):
    DEBUG = True


class Parser():
    def __init__(self):
        self.all_news = []

    def get_normal_time(self, time):
        return datetime.datetime.fromtimestamp(time).strftime('%H:%M %d.%m.%Y')

    @staticmethod
    def get_unix_time(self, element):
        pass

    @staticmethod
    def instructions(self, element):
        pass

    def data_form(self, section, href, title, text, time):
        data = {"name": self.name,
                "section": section,
                "link": href,
                "header": title,
                "text": text,
                "time": time,
                "norm_time": self.get_normal_time(time)}
        return data

    def get_news(self):
        for i in self.pages:
            self.url = i[0]
            session = requests.Session()
            connect = session.get(self.url, headers=headers)
            html = BS(connect.content, 'html.parser')

            for element in html.find_all(self.obj, class_=re.compile(self.value)):
                try:
                    info = self.instructions(element)
                except Exception:
                    continue
                data = self.data_form(i[1], info[0], info[1], info[2], info[3])
                self.all_news.append(data)


class Tut(Parser):
    name = 'tut.by'

    def __init__(self):
        super().__init__()
        self.name = Tut.name
        self.obj = 'div'
        self.value = 'news-entry big annoticed time ni'
        self.pages = [['https://news.tut.by/daynews', 'daynews'], ['https://news.tut.by/auto', 'auto'],
                      ['https://news.tut.by/realty', 'realt']]

    def get_unix_time(self, element):
        return int(element.find('span', attrs={'class': 'entry-time'}).next_element.get("data-ctime"))

    def instructions(self, element):
        href = element.find('a', attrs={'class': 'entry__link'})['href']
        title = element.find('span', attrs={'class': 'entry-head _title'}).text.replace('\xa0', ' ')
        text = element.find('span', attrs={'class': 'entry-note'}).text.replace('\xa0', ' ')
        time = self.get_unix_time(element)
        return [href, title, text, time]


class RussiaToday(Parser):
    name = 'russian.rt.com'

    def __init__(self):
        super().__init__()
        self.name = RussiaToday.name
        self.obj = 'li'
        self.value = 'listing__column listing__column_all-new'
        self.pages = [['https://russian.rt.com/news', 'daynews'], ['https://russian.rt.com/opinion', 'opinion'],
                      ['https://russian.rt.com/trend/335010-tehnologii', 'tech']]

    def get_unix_time(self, element):
        try:
            time = element.find('time').get("datetime")
        except Exception:
            time = ' '.join(element.find('div', class_=re.compile('card__date card__date_all-news')).text.split())
            time = datetime.datetime.now().strftime('%Y-%m-%d ') + time
        return int(datetime.datetime.strptime(time, '%Y-%m-%d %H:%M').timestamp())

    def instructions(self, element):
        if 'https://russian.rt.com/news' == self.url:
            links = element.find_all('a', class_=re.compile('link link_color'))
            href = self.url[:22] + links[1]['href']
            title = ' '.join(links[1].text.split())
            text = ' '.join(links[2].text.split())
        else:
            href = self.url[:22] + element.find('a', class_=re.compile('link link_color'))['href']
            title = ' '.join(element.find('a', class_=re.compile('link link_color')).text.split())
            text = ' '.join(element.find('div', class_=re.compile('card__summary card__summary_all-new')).text.split())
        time = self.get_unix_time(element)
        return [href, title, text, time]


class Onliner(Parser):
    name = 'onliner.by'

    def __init__(self):
        super().__init__()
        self.name = Onliner.name
        self.obj = 'div'
        self.value = 'news-tidings__item news-tidings__item_1of3'
        self.pages = [['https://people.onliner.by/opinions', 'opinion'],
                      ['https://auto.onliner.by', 'auto'], ['https://tech.onliner.by', 'tech'],
                      ['https://realt.onliner.by', 'realt']]

    def get_unix_time(self, element):
        yesterday = '0' + str(int(datetime.datetime.now().strftime('%d')[1]) - 1)
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

        time = ' '.join(element.find('div', attrs={'class': 'news-tidings__time'}).text.split())
        if 'Сегодня в ' in time:
            time = datetime.datetime.now().strftime('%Y-%m-%d ') + time[10:]
        elif 'Вчера в ' in time:
            time = datetime.datetime.now().strftime('%Y-%m-') + yesterday + ' ' + time[8:]
        else:
            time = time.split()
            time = time[2] + '-' + str(months.index(time[1]) + 1) + '-' + time[0] + ' ' + time[-1]
        return int(datetime.datetime.strptime(time, '%Y-%m-%d %H:%M').timestamp())

    def instructions(self, element):
        href = self.url + element.find('a', attrs={'class': 'news-tidings__link'})['href']

        try:
            title = ' '.join(element.find('span', attrs={'class': 'news-helpers_hide_mobile-small'}).text.split())
        except Exception:
            title = ' '.join(element.find('a', attrs={'class': 'news-tidings__link'}).text.split())

        text = element.find('div', attrs={'class': 'news-tidings__speech news-helpers_hide_mobile-small'}).text
        text = ' '.join(text.split())

        time = self.get_unix_time(element)
        return [href, title, text, time]


class iXBT(Parser):
    name = 'ixbt.com'

    def __init__(self):
        super().__init__()
        self.name = iXBT.name
        self.obj = 'div'
        self.value = 'item no-padding'
        self.pages = [['https://www.ixbt.com/news/?show=tape', 'tech_daynews']]

    def get_unix_time(self, element):
        time = datetime.datetime.now().strftime('%Y-%m-%d ') + element.find('span').text
        time = int(datetime.datetime.strptime(time, '%Y-%m-%d %H:%M').timestamp())
        if int(tm.time()) < time:
            print(1)
            time -= 86400
        return time

    def instructions(self, element):
        href = self.url[:20] + element.find('a', attrs={'id': ''})['href']
        title = element.find('a', attrs={'id': ''}).text
        text = element.find('h4').text
        time = self.get_unix_time(element)
        return [href, title, text, time]
