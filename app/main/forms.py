from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators = [Required()])
    description = TextAreaField('Pitch description', validators = [Required()])
    category = category = SelectField('Select category', choices=[('life-lessons', 'Life lessons'), ('entertainment', 'Entertainment'), ('motivational', 'Motivational')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('What inspires you??',validators = [Required()])
    submit = SubmitField('Update')

class CommentForm(FlaskForm):
    comment = TextAreaField('Give feedback', validators=[Required()])
    submit = SubmitField('Post')