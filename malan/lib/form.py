from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, ValidationError

class SearchForm(FlaskForm):
    string = StringField('SearchString', validator=[DataRequired()])
    submit = SubmitField('Search')

class FileForm(FlaskForm):
    testfile = MultipleFileField('Files')
    submit = SubmitField('Diagnosis')

    def validate_testfile(self, testfile):
        if len(testfile.data) == 1 and testfile.data[0].filename=='':
            raise ValidationError("This field is required.")
