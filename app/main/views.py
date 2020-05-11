from . import main
from flask import render_template,request,redirect,url_for, abort
from ..models import Blog, Comment, User
from flask_login import login_required,current_user
from .. import db, photos
from .forms import BlogForm,UpdateProfile, CommentForm

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to My Blog'
    return render_template('index.html' , title = title)