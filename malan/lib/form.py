from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, ValidationError

class SearchForm(FlaskForm):
    string = StringField('SearchString', validator=[DataRequired()])
    submit = SubmitField('Search')

class FileForm(FlaskForm):
    test_file = MultipleFileField('Files')
    submit = SubmitField('Diagnosis')

    def validate_test_file(self, test_file):
        if len(test_file.data) == 1 and test_file.data[0].filename=='':
            raise ValidationError("This field is required.")
