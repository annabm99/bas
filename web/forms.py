# Page to make forms for users to fill (to register, for example)
#from flask_wtf import FlaskForm # Specific flask package to make forms
#from wtforms import StringField, TextAreaField, SelectMultipleField, FileField, SubmitField # Importing a certain type of field for the forms
#from wtforms.validators import EqualTo, DataRequired, Optional, ValidationError, Email# Validators for our form's requirements

#def allowed_file(inputfile):
#    return "." in inputfile and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

#class SequenceForm(FlaskForm): # Inherits from the Flask form class
    
    # INPUT
 #   sequences = TextAreaField(label="Sequences (FASTA format):", validators=[Optional()]) # The label is what will be displayed as header for the field
 #   ids = StringField(label="Uniprot IDs:", validators=[Optional(), Email()])
 #   inputfile = FileField(label="Upload File (FASTA format):", validators=[Optional()]) # Different type of field for passwords

    # OPTIONS
 #   outputformat = SelectMultipleField(label="Choose output format:", choices = ["fasta", "clustal", "msf", "phylip", "stockholm", "vienna"], validators=[DataRequired()])

    # SUBMIT
 #   submit = SubmitField(label="Submit")

 #   def validate(self):
 #       if (self.outputformat.data.first() == "fasta"):
  #             raise ValidationError("No input was provided")
  #      if not (self.sequences.data or self.ids.data or self.inputfile.data):
  #          raise ValidationError("No input was provided")

# Page to make forms for users to fill (to register, for example)
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