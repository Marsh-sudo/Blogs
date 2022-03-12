from flask import Blueprint,render_template

gg = Blueprint('gg',__name__)

@gg.route('/')
def home():
    return render_template("home.html")

