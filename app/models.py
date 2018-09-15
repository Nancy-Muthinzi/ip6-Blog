from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
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

# class Comment(db.Model):

#     __tablename__ = 'comments'

#     id = db.Column(db.Integer,primary_key = True)
#     comment= db.Column(db.String)
#     blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
#     username =  db.Column(db.String)
#     votes= db.Column(db.Integer)

#     def save_comment(self):
#         '''
#         Function that saves comments
#         '''
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def clear_comments(cls):
#         Comment.all_comments.clear()

#     @classmethod
#     def get_comments(cls,id):
#         comments = Comment.query.filter_by(blog_id=id).all()

#         return comments