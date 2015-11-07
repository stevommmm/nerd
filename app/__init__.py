# Import flask and template operators
from flask import Flask, render_template, send_file, redirect

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import urllib and os for our skin proxy
import urllib, os, time

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Import our models now that we have a handle to `db`
from app.models import Player


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def route_index():
	import random
	return render_template('index.html', players_online=random.randint(0, 100))

@app.route('/u/', methods=['GET'])
def route_users():
	db_players = Player.query.order_by(Player.last_login.desc()).limit(1000).all()
	print(db_players)
	return render_template('users.html', players=db_players)

@app.route('/u/<string:player>', methods=['GET'])
def route_user(player):
	db_player = Player.query.filter_by(name=player).first_or_404()
	return render_template('user.html', player=db_player)

@app.route('/_skin/<string:player>', methods=['GET'])
def route_user_skin(player):
	floc = os.path.join(app.config['SKIN_CACHE'], player + '.png')

	def fetch_skin():
		url = '''http://skins.minecraft.net/MinecraftSkins/{username}.png'''
		f = urllib.request.urlopen(url.format(username=player))
		return f.read()

	def is_stale_skin():
		"""We should request a new skin if its older than 30 days"""
		return time.time() - os.path.getmtime(floc) > (30 * 24 * 60 * 60)

	if not os.path.exists(floc) or is_stale_skin():
		try:
			skin_data = fetch_skin()
			with open(floc, 'wb+') as ouf:
				ouf.write(skin_data)
		except urllib.error.HTTPError:
			return redirect('/_skin/default')

	return send_file(floc, mimetype='image/png')


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()