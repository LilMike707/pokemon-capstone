from flask import Flask, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Like
from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pokemon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "mikeisabeast"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
db.create_all()

# toolbar = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return redirect('/home')


@app.route('/home')
def show_home():
    return render_template('home.html')

@app.route('/login')
def show_login():
    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def show_register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        db.session.commit()

        return redirect('/home')



    return render_template('register.html', form=form)

@app.route('/liked-cards')
def show_likes():

    return render_template('liked.html')