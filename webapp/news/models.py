from datetime import datetime
from sqlalchemy.orm import relationship
from webapp.db import db


class News(db.Model): # атрибуты, поля в таблице
    id = db.Column(db.Integer, primary_key=True)  # целое число, первичный ключ, бд будет его индексировать
    title = db.Column(db.String, nullable=False)  # nullable -может ли это значение не быть в сопоставляемых данных, просим БД проверять нас
    url = db.Column(db.String, unique=True, nullable=False)  # unique - url у каждой новости уникальный
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def comments_count(self):
        return Comment.query.filter(Comment.news_id == self.id).count()

    def __repr__(self):  # магический метод, чтобы в дальнейшем при получении обьекта понимать, что это за объект
        return '<News {} {}>'.format(self.title, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    news_id = db.Column(
        db.Integer,
        db.ForeignKey('news.id', ondelete='CASCADE'),  # поведение поля при удалении новости
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    news = relationship('News', backref='comments')
    user = relationship('User', backref='comments')

    def __repr__(self):
        return '<Comment {}>'.format(self.id)

