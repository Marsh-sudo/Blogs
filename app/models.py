
from flask_login import UserMixin,current_user
from . import db
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique= True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    blog = db.relationship('Blog')

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(20000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


