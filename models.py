from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()


bcrypt = Bcrypt()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    likes = db.relationship('Like', backref = 'user', lazy=True)

    # def set_password(password):
    #     return bcrypt.generate_password_hash(cls, password).decode('utf-8')
    
    # def check_password(password):
    #     return bcrypt.check_password_hash(self.password, password)
    @classmethod 
    def register(cls, username, password):
        print(f'username is {username}')
        hashed = bcrypt.generate_password_hash(password)

        hash_str = hashed.decode("utf8")

        return cls(username=username, password=hash_str) 


class Like(db.Model):

    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.Integer, nullable=False)


def connect_db(app):
    db.app = app
    db.init_app(app)
    
