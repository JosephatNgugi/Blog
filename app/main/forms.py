from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
    title = StringField("Blog Title", validators=[InputRequired()])
    blog = TextAreaField('Share Your Blog', validators=[InputRequired()])
    submit = SubmitField('Post')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Share your Thoughts',validators=[InputRequired()])
    submit = SubmitField('Comment')
    