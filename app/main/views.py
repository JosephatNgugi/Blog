from flask import render_template

from ..request import get_quote
from ..models import Blog
from . import main

@main.route("/")
def index():
    blogs = Blog.query.all()
    quotes = get_quote()
    title = 'Home: Blog'
    
    return render_template("index.html", title=title, blogs=blogs, quotes=quotes)