### This file will be run every time the app is executed
### This allows to call it from other files, because it will always have executed first

from flask import Flask, render_template # Import flask instance from Flask package
from flask_sqlalchemy import SQLAlchemy # Package needed to create the database
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

# render_template is to address templates (html)
app = Flask (__name__,
            static_url_path='', 
            static_folder='./static',
            template_folder='./templates')

app.config['SECRET_KEY'] = '34d60585b853a486c59090bf'
app.config['UPLOAD_FOLDER'] = './'
app.config['ALLOWED_EXTENSIONS'] = set(['*.fa', '*.fasta'])

hostedApp = Flask (__name__,
            static_url_path='', 
            static_folder='./static',
            template_folder='./templates')

hostedApp.config['SECRET_KEY'] = '34d60585b853a486c59090bf'
hostedApp.config['UPLOAD_FOLDER'] = './'
hostedApp.config['ALLOWED_EXTENSIONS'] = set(['*.fa', '*.fasta'])
hostedApp.wsgi_app = DispatcherMiddleware(NotFound(), {f"/u194046":app})

from web import routes # Import routes (from the routes file)