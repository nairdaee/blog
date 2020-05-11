from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    blog = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String, nullable=False)
    comments = db.relationship('Comment', backref='blog', lazy='dynamic')
      #upvotes = db.relationship('Upvote', backref='blog', lazy='dynamic')
      #downvotes = db.relationship('Downvote', backref='blog', lazy='dynamic')
    posted_p = db.Column(db.DateTime,default=datetime.utcnow)
    user_p = db.Column(db.Integer,db.ForeignKey("users.id"),  nullable=False)
    
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,id):
        blogs = Blog.query.order_by(blog_id=id).desc().all()
        return blogs

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted_c = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"), nullable=False)
    user_c = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(blog_id=id).all()
        return comments


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
      #upvotes = db.relationship('Upvote', backref='user', lazy='dynamic')
      #downvotes = db.relationship('Downvote', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'
