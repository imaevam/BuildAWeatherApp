from webapp.news.models import News
from webapp.weather import weather_by_city
from flask import Blueprint, render_template, current_app


blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    title = "Новости Python"
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_list = News.query.order_by(News.published.desc()).all() # верни нам все новости из БД 
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)
    
