from webapp.db import db

class News(db.Model): # атрибуты, поля в таблице
    id = db.Column(db.Integer, primary_key=True) # целое число, первичный ключ, бд будет его индексировать
    title = db.Column(db.String, nullable=False) # nullable -может ли это значение не быть в сопоставляемых данных, просим БД проверять нас
    url = db.Column(db.String, unique=True, nullable=False) #unique - url у каждой новости уникальный
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self): # магический метод, чтобы в дальнейшем при получении обьекта понимать что это за объект
        return '<News {} {}>'.format(self.title, self.url)
