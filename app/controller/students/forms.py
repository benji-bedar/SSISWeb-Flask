from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import app.models.student as models

class StudentForm(FlaskForm):
    avatar_url = StringField("Avatar Url", [validators.DataRequired()])
    id_number = StringField("ID Number", [validators.DataRequired()])
    first_name = StringField("First Name", [validators.DataRequired()])
    last_name = StringField("Last Name", [validators.DataRequired()])
    course_id = StringField("Course", [validators.DataRequired()])
    year = StringField("Year", [validators.DataRequired()])
    gender = StringField("Gender", [validators.DataRequired()])
    submit = SubmitField("Submit")
