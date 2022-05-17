from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from . import main
from ..request import get_quote
from .forms import BlogForm, CommentForm
from ..models import Blog, Comment


@main.route("/")
def index():
    blogs = Blog.query.all()
    quotes = get_quote()
    title = 'Home: Blog'
    
    return render_template("index.html", title=title, blogs=blogs, quotes=quotes)

@main.route("/pitch/new-pitch", methods=['GET', 'POST'])
@login_required
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        category=form.category.data
        title=form.title.data
        blog=form.blog.data
        user_id = current_user
        new_blog= Blog(category=category, title=title,blog=blog, user=user_id)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    title = 'Create New Pitch'
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