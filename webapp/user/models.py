from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 

from webapp.db import db

class User(db.Model, UserMixin): #множественное наследование; def is_authenticated и тд
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True) # ограничение по длине; те, колонки по которым в дальнейшем будем фильтровать запросы имеет смысл делать индексами, т.к. поиск по индексу быстрее
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password) #true \ false

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return 'User name={} id={}'.format(self.username, self.id)
