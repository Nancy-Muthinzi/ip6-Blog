from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    category = StringField('Blog category',validators=[Required()])
    content = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Create')