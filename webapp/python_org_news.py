from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url) # берем данные из url
        result.raise_for_status() # при возникновении проблемы будет ошибка
        return result.text # контент страницы
    except(requests.RequestException, ValueError): #requestexception - сетевая проблема
        print("Network error")
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts') #recent posts
        all_news = all_news.findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)

def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count() #проверка, чтобы не было совпадений
    print(news_exist)    #count дает количество объектов, попадающих под этот запрос
    if not news_exist:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()

#создали обьект News, передали ему значения, которые мы хотим сохранить в БД, add(можно несколько раз), commit
