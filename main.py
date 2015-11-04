"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template
from flask.ext.bower import Bower
app = Flask(__name__, static_path='/static')
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')


@app.route('/login')
def login():
    return 'Nothing here'


@app.route('/email')
def email():
    return 'nothing here'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


Bower(app)
