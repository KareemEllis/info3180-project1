from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, DecimalField, FloatField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect

class NewPropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = PasswordField('Description', validators=[InputRequired()])
    num_rooms = IntegerField('Number of Rooms', validators=[InputRequired()])
    num_bathrooms = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()], places=2)
    property_type = StringField('Property Type', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])