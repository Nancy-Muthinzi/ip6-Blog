from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

# class CommentForm(FlaskForm):
#     category = StringField('Comment Title',validators=[Required()])
#     content = TextAreaField('Comment', validators=[Required()])
#     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
 title = StringField('Comment title',validators=[Required()])
 review = TextAreaField('Blog comment')
 submit = SubmitField('Submit')    