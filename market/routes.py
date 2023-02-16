from market import app # Importing the app
from flask import render_template, redirect, url_for, flash # Import package to read templates
from market.models import Item, User # Import Item from the database
from market.forms import SequenceForm # Import register form from the forms file
from werkzeug.utils import secure_filename
import os


# HOMEPAGE
@app.route("/") # Root url
@app.route("/home") # Root url
def home_page():
    return render_template("home.html") # Flask function that redirects to html file (it has to be imported previously)

# DYNAMIC ROUTE
@app.route("/about/<username>")
def about_page(username):
    return f"<h1>This is the about page of {username}</h1>"

@app.route("/input")
def input_page():
    name = "Anna"
    return render_template('input.html', item=name)
    # Whatever is put into name will be sent to the html jinja, and it will be displayed on the webpage


@app.route("/market")
def market_page():
    items = Item.query.all() # Refers to the Item table from the database, which will be displayed on the page
    return render_template("market.html", items=items)

# CLUSTAL PAGE
@app.route("/clustalo", methods=["GET", "POST"]) # This route can support get and post requests
def clustal_app():
    form = SequenceForm() # Referring to register form in the forms.py file
    if form.validate_on_submit:
        sequences = form.sequences.data
        ids = form.sequences.data

    # Display fields of the form, through register.html file
    return render_template("clustalo.html", form=form)