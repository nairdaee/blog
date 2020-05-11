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