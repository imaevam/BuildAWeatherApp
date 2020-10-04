from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash 

db = SQLAlchemy()

class News(db.Model): # атрибуты, поля в таблице
    id = db.Column(db.Integer, primary_key=True) # целое число, первичный ключ, бд будет его индексировать
    title = db.Column(db.String, nullable=False) # nullable -может ли это значение не быть в сопоставляемых данных, просим БД проверять нас
    url = db.Column(db.String, unique=True, nullable=False) #unique - url у каждой новости уникальный
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self): # магический метод, чтобы в дальнейшем при получении обьекта понимать что это за объект
        return '<News {} {}>'.format(self.title, self.url)

class User(db.Model, UserMixin): #множественное наследование; def is_authenticated и тд
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True) # ограничение по длине; те, колонки по которым в дальнейшем будем фильтровать запросы имеет смысл делать индексами, т.к. поиск по индексу быстрее
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password) #true \ false

    def __repr__(self):
        return 'User {}'.format(self.username)

    


