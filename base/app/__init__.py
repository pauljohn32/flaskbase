import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#from config import Config

app = Flask(__name__)

print("OS environment", os.environ.get("FLASK_ENV"))

if os.environ.get("FLASK_ENV") == "development":
    print("OS environment development:", os.environ.get("FLASK_ENV"))
    app.config.from_object('config.DevConfig')
else:
    app.config.from_object('config.ProdConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'


from app import routes, models
