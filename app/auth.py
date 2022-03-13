
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=["GET","POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html",text="testing")

@auth.route('/logout')
def logout():
    return "logout"

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
            # add user
            flash('Your account has been created successfully',category='success')

    return render_template("sign_up.html")