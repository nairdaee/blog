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

@main.route('/<cat>', methods=['GET', 'POST'])
def pickup(cat):
    cat = cat
    blogs = Blog.query.filter_by(category=cat).order_by(Blog.posted_p.desc()).all()
    return render_template('category.html', blogs=blogs)

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        user_p = current_user
        category = form.category.data

        new_blog = Blog(user_p=current_user._get_current_object().id, title=title, category=category, description = description)

        new_blog.save_blog()
        blogs = Blog.query.filter_by(category=category).order_by(Blog.posted_p.desc()).all()
        return render_template('category.html', blogs=blogs)
    return render_template('new_blog.html', form=form)


@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)

    if form.validate_on_submit():
        comment = form.comment.data
         
        # Updated comment instance
        new_comment = Comment(comment=comment,user_c=current_user._get_current_object().id, blog_id=blog_id)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',blog_id = blog_id ))

    all_comments = Comment.query.filter_by(blog_id=blog_id).all()
    return render_template('comment.html', form=form, comments=all_comments, blog=blog)

@main.route('/myblogs', methods=['GET', 'POST'])
@login_required
def my_blogs():
    user = current_user._get_current_object().id
    blogs = Blog.query.filter_by(user_p=user)
    return render_template('category.html', blogs=blogs)
    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files: 
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.index', uname = uname))