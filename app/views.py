from crypt import methods
from flask import Blueprint,render_template

gg = Blueprint('gg',__name__)

@gg.route('/')
def home():
    return render_template("home.html")

@gg.route('/new-blog')
def blog():
    return render_template("blog.html")

