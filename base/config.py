import os
import dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#dotenv.load_dotenv(os.path.join(basedir, ".flaskenv"))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") 
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = 'static'
 
class ProdConfig(Config):
    # fname = os.environ.get('DEV_DATABASE_URL')
    fname = 'app.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, fname)
##    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
##  or \
##        'sqlite:///' + os.path.join(basedir, 'app.db')

class DevConfig(Config):
    DEBUG = True
    TESTING = True
    # fname = os.environ.get('DEV_DATABASE_URL')
    # print(fname)
    fname = 'app.db'
    print("fname", fname)
    print("basedir", basedir)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, fname)

    # os.environ.get('DEV_DATABASE_URI') or \
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


