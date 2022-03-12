
from flask import Flask 
from  flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']

    #initializing bootstrap
    bootstrap.init_app(app)

    from .views import gg
    from .auth import auth

    app.register_blueprint(gg,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app