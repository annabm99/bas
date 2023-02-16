# Page to make forms for users to fill (to register, for example)
from flask_wtf import FlaskForm # Specific flask package to make forms
from wtforms import StringField, TextAreaField, SelectMultipleField, FileField, SubmitField # Importing a certain type of field for the forms
from wtforms.validators import Length, EqualTo, Email, DataRequired # Validators for our form's requirements
from market.models import User

def allowed_file(inputfile):
    return "." in inputfile and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

class SequenceForm(FlaskForm): # Inherits from the Flask form class
    # INPUT
    sequences = TextAreaField(label="Sequences (FASTA format):") # The label is what will be displayed as header for the field
    ids = StringField(label="Uniprot IDs:")
    inputfile = FileField(label="Upload File (FASTA format):") # Different type of field for passwords

    # OPTIONS
    outputformat = SelectMultipleField(label="Choose output format:", choices = ["ClustalW", "Pearson/FASTA"])

    # SUBMIT
    submit = SubmitField(label="Submit")
