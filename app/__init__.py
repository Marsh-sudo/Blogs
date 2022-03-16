from importlib.resources import path
from flask import Flask 
from  flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
DB_NAME = "database.db"
mail = Mail()

bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    mail.init_app(app)

    #initializing bootstrap
    bootstrap.init_app(app)
    

    from .views import gg
    from .auth import auth

    app.register_blueprint(gg,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Blog

   

    return app

  