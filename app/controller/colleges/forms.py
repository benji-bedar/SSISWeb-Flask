from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField

class CollegeForm(FlaskForm):
    code = StringField('Code', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    submit = SubmitField("Submit")
