from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from . import main
from ..request import get_quote
from .forms import BlogForm
from ..models import Blog


@main.route("/")
def index():
    blogs = Blog.query.all()
    quotes = get_quote()
    title = 'Home: Blog'
    
    return render_template("index.html", title=title, blogs=blogs, quotes=quotes)

@main.route("/", methods=['GET', 'POST'])
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
    return render_template('index.html', form=form)