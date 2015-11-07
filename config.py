# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Skin cache
SKIN_CACHE = os.path.join(BASE_DIR, 'skincache')
if not os.path.exists(SKIN_CACHE):
	os.mkdir(SKIN_CACHE)

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "eabb41adeb214b28ab4fe9925de3a432"

# Secret key for signing cookies
SECRET_KEY = "850fb5b559b7482294e9699dee874eb5"