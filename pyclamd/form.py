from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    string = StringField('SearchString', validator=[DataRequired()])
    submit = SubmitField('Search')

class FileForm(FlaskForm):
    testfile = FileField('Files')
    submit = SubmitField('Diagnosis')
