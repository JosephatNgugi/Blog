from flask import render_template, redirect, url_for, abort
from flask_login import current_user, login_required
from . import main
from ..request import get_quote
from .forms import BlogForm, CommentForm, UpdateProfile
from ..models import Blog, Comment, User



@main.route("/")
def index():
    blogs = Blog.query.all()
    quotes = get_quote()
    title = 'Home: Blog'
    
    return render_template("index.html", title=title, blogs=blogs, quotes=quotes)

@main.route("/user/<uname>")
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route("/user/<uname>/update",methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username =uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    if form.validate_on_submit():
        user.about = form.about.data
        user.save_user()
        
        return redirect(url_for(".profile",uname=user.username))
    return render_template('profile/update.html', form =form)

@main.route("/new-pitch", methods=['GET', 'POST'])
@login_required
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title=form.title.data
        blog=form.blog.data
        user_id = current_user
        new_blog= Blog(title=title,blog=blog, user=user_id)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    title = 'Create New Blog'
    return render_template('index.html', title=title, form=form)

@main.route('/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blog_id = blog.id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id =user_id, blog_id =blog_id)      
        new_comment.save_comment()
        return redirect(url_for('.comment', blog_id =blog_id))
    return render_template('comment.html', form=form, blog=blog, comments=comments)