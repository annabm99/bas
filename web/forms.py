from flask_wtf import FlaskForm # Specific flask package to make forms
from wtforms import StringField, TextAreaField, FileField, SubmitField, SelectMultipleField # Importing a certain type of field for the forms
from wtforms.validators import DataRequired, Optional, ValidationError # Validators for our form's requirements

class SequenceForm(FlaskForm): # Inherits from the Flask form class
    
        
    # If more than one validator, they can be put in a list
    # Email validator checks for email sign, datarequired checks if in fact there is data in the field
    sequences = TextAreaField(label="Sequences (FASTA format):", validators=[Optional()]) # The label is what will be displayed as header for the field
    ids = StringField(label="Uniprot IDs (format: id1, id2, ...):", validators = [Optional()])
    inputfile = FileField(label="Upload a FASTA file:", validators=[Optional()]) # Different type of field for passwords
    outputformat = SelectMultipleField(label="Choose an output format:", choices = ["fasta", "clustal", "msf", "phylip", "stockholm", "vienna"], validators=[DataRequired()]) # For password validation: it has to be equal to the 1st
    
    submit = SubmitField(label="Sumbit")