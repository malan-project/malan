from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    string = StringField('SearchString', validator=[DataRequired()])
    submit = SubmitField('Search')

class FileForm(FlaskForm):
    testfile = MultipleFileField('Files')
    submit = SubmitField('Diagnosis')
