from app import app, db
from models import User, Like
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# # create users
# user1 = User(username='Alice', password=bcrypt.generate_password_hash(
#     'password').decode('utf-8'))
# user2 = User(username='Bob', password=bcrypt.generate_password_hash(
#     'password').decode('utf-8'))
# user3 = User(username='Charlie', password=bcrypt.generate_password_hash(
#     'password').decode('utf-8'))
# user4 = User(username='Dave', password=bcrypt.generate_password_hash(
#     'password').decode('utf-8'))
# user5 = User(username='Eve', password=bcrypt.generate_password_hash(
#     'password').decode('utf-8'))

# # add users to session
# db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)
# db.session.add(user4)
# db.session.add(user5)

# # commit changes to the database
# db.session.commit()

# create likes associated with each user
like1 = Like(user_id=1, card_id='base1-23')
like2 = Like(user_id=1, card_id='base1-25')
like3 = Like(user_id=1, card_id='base1-21')
like4 = Like(user_id=1, card_id='base1-26')
like5 = Like(user_id=1, card_id='base1-27')

# add likes to session
db.session.add(like1)
db.session.add(like2)
db.session.add(like3)
db.session.add(like4)
db.session.add(like5)

# commit changes to the database
db.session.commit()
