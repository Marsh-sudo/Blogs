from .models import User
from flask import Blueprint,render_template,request,flash,redirect,url_for
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,current_user,login_required

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user =User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password,try again',category='error')
        else:
                flash('Email does not exist',category='error')
   
    return render_template("login.html",text="testing")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if len(email) < 4:
            flash('Unscalable email address',category='error')
        elif len(username) <2:
            flash('Short Username',category='error')
        elif len(password) < 7:
            flash('Short password!!!',category='error')
        else:
            new_user = User(email=email,username=username,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user=True,remember=True)
             
            flash('Your account has been created successfully',category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")