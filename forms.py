from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    
    name = StringField("Pet Name", validators=[InputRequired('Please enter a name')])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(0, 30)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    
class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(0, 30)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available")