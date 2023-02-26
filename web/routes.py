#! usr/bin/env python

from web import app # Importing the app
from flask import render_template, redirect, url_for, flash # Import package to read templates
from web.forms import SequenceForm # Import register form from the forms file
from werkzeug.utils import secure_filename
import os
from web import process


# HOMEPAGE
@app.route("/") # Root url
@app.route("/home") # Root url
def home_page():
    return render_template("index.html") # Flask function that redirects to html file (it has to be imported previously)

@app.route("/clustalo", methods=["GET", "POST"]) # This route can support get and post requests
def clustal_app():
    form = SequenceForm() # Referring to register form in the forms.py file
    # This will only be executed if the user clicks on the validate button from the form:
    if form.validate_on_submit():
        sequences = form.sequences.data
        if sequences:
            process.process_sequences(sequences)
        id_list = form.ids.data
        if id_list:
            process.process_uniprot(id_list) 
        clustal_input_file = form.inputfile.data
        if clustal_input_file:
            clustal_input_file.save(secure_filename("input.fasta"))       
        output_format = form.outputformat.data
        process.execute_clustalo(output_format[0])
        return redirect(url_for("clustal_done"))
    if form.errors != {}: # if form.errors is not empty, check for errors
        for err_msg in form.errors.values(): # go through error messages
            # Instead of printing to the terminal, flash prints to the user interface so users can be aware of errors
            flash(f"There was an error in creating the user: {err_msg}")
    # Display fields of the form, through register.html file
    return render_template("clustalo.html", form=form)

@app.route("/clustalo/output")
def clustal_done():
    with open ("outfile", "r") as f:
        content = f.read()
    return render_template('done.html', content=content)

@app.route("/datamodel")
def data_model():
    return render_template("datamodel.html")

@app.route("/wikipop")
def wikipop():
    return render_template("wikipop.html")