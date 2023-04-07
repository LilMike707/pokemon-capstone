from flask import Flask, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Like
from forms import LoginForm, RegisterForm
import requests, random

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pokemon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "mikeisabeast"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

API_KEY = '86d009f1-34fa-4d94-9888-7eae05f5fc1f'
BASE_URL = 'https://api.pokemontcg.io/v2/'


connect_db(app)
db.create_all()

# toolbar = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    return redirect('/home')


@app.route('/home')
def show_home():
    if 'curr_user' in session:
        id = session['curr_user']
        user = User.query.filter_by(id=id).first()
        return render_template('home.html', user=user)
    else:
        user = ''
        return render_template('home.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def show_login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session['curr_user'] = user.id
            flash('You Logged In!')
            return redirect('/home')
        else:
            return redirect('/liked_cards')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
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


@app.route('/<int:id>/likes')
def show_likes(id):
    # if 'curr_user' in session:
    # user = User.query.filter_by(id=user_id).first()
    likes = Like.query.filter_by(user_id=id).all()  # This might not work?
    return render_template('liked.html', likes=likes)


def get_setlist():
    url = f'{BASE_URL}sets'
    sets = []
    headers = {'x-api-key':API_KEY}
    response = requests.get(url, headers=headers)
    raw_data = response.json()
    data = raw_data['data']
    for card_set in data:
        name = card_set['name']
        id = card_set['id']
        sets.append({
            'id':id,
            'name':name
        })
    return sets[:14]


def get_setlist_index():
    url = f'{BASE_URL}sets'
    sets = []
    headers = {'x-api-key':API_KEY}
    response = requests.get(url, headers=headers)
    raw_data = response.json()
    data = raw_data['data']
    for card_set in data:
        sets.append(card_set)
    return sets[:14]

@app.route('/index')
def show_index():
    sets = get_setlist_index()
    return render_template('set_index.html', sets=sets)


@app.route('/index/<set_id>')
def show_set(set_id):
    sets = get_setlist()
    url = f'{BASE_URL}cards?q=set.id:{set_id}'
    cards = []
    headers = {'x-api-key':API_KEY}
    response = requests.get(url, headers=headers)
    raw_data = response.json()
    data = raw_data['data']
    for card in data:
        cards.append(card)
    random_cards = random.sample(cards,50)
    return render_template('index.html', sets=sets, cards=random_cards)    

