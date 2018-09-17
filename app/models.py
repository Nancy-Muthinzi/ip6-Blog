from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(255))
    blog_post = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')


    def set_password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'        


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    username =  db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()

        return comments