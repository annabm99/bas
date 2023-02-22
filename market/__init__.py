### This file will be run every time the app is executed
### This allows to call it from other files, because it will always have executed first

from flask import Flask, render_template # Import flask instance from Flask package
from flask_sqlalchemy import SQLAlchemy # Package needed to create the database

# render_template is to address templates (html)
app = Flask(__name__) # Variable referring to the local Python file
# Make Flask recognise a database:
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db' # Dictionary that will access some given key value (the thing inside [] is the key value)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            # These key values are conventions to read database in Python
            # It is pointed to where the database file is stored (market.db )
app.config['SECRET_KEY'] = '34d60585b853a486c59090bf'
db = SQLAlchemy(app) # Call the database variable
app.app_context().push() # Needed to modify the db
app.config['UPLOAD_FOLDER'] = './'
app.config['ALLOWED_EXTENSIONS'] = set(['*.fa', '*.fasta'])

from market import routes # Import routes (from the routes file)