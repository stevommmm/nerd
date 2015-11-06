# Import flask and template operators
from flask import Flask, render_template, send_file

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import urllib for our skin proxy
import urllib

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def route_index():
	import random
	return render_template('index.html', players_online=random.randint(0, 100))

@app.route('/u/<string:player>', methods=['GET'])
def route_user(player):
	return render_template('user.html', player=player)

@app.route('/_skin/<string:player>', methods=['GET'])
def route_user_skin(player):
	url = '''http://s3.amazonaws.com/MinecraftSkins/{username}.png'''.format(username=player)
	f = urllib.request.urlopen(url)
	return send_file(f, mimetype='image/png')


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()