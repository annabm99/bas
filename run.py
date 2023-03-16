from web import hostedApp as app # call app variable from the init file.

if __name__=='__main__': # Command to run the app
    app.run(debug=False) # True so we can see edits real-time