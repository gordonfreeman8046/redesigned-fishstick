from lorem_text import lorem
app = lorem(__name__)
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from lorem_text import lorem

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message=lorem.paragraph()
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message=lorem.paragraphs(5)
    )

"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import FlaskWebProject1.views
"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "C:/ftp_directory", perm="elradfmw")  # Set FTP credentials and directory
    authorizer.add_anonymous("C:/ftp_directory", perm="elr")  # Allow anonymous read-only access

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 21), handler)  # Host on port 21
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()

