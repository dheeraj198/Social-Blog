from flask_sqlalchemy import SQLAlchemy
from blogs import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
from blogs import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):

    __tablename__  = 'users'

    id = db.Column(db.Integer,primary_key = True)
    profile_image = db.Column(db.String(64),nullable = False , default = 'default_profile.png')
    username = db.Column(db.String(64),unique = True , index = True)
    email = db.Column(db.String(64),unique = True , index = True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('BlogPosts',backref = 'author' , lazy = True)

    def __init__(self,username,email,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'Username : {self.username}'

class BlogPost(db.Model):

    users = db.relationship(User)
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    date = db.Column(db.DateTime,nullable=False,default = datetime.utcnow)
    title = db.Column(db.String(140) , nullable=False)
    text = db.Column(db.Text , nullable=False)

    def __init__(self,title,text,user_id):
        self.text = text
        self.title = title
        self.user_id = user_id

    def __repr__(self):
        return f"PostID: {self.id}"