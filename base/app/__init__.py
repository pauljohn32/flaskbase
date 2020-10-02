import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


#from config import Config

## app = Flask(__name__)

print("OS environment", os.environ.get("FLASK_ENV"))


db = SQLAlchemy()
migrate = Migrate()

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = "Please log in"

mail = Mail()

def create_app():
    
    app = Flask(__name__, instance_relative_config=False)

    if os.environ.get("FLASK_ENV") == "development":
        print("OS environment is DEVELOPMENT: ", os.environ.get("FLASK_ENV"))
        app.config.from_object('config.DevConfig')
    else:
        print("OS environment is PRODUCTION: ", os.environ.get("FLASK_ENV"))
        app.config.from_object('config.ProdConfig')
   
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    
    # with app.app_context():

    #     app.register_blueprint(auth.auth_bp)
    #     app.register_blueprint(main.main_bp)

    #     return app
    print("app.register now:")
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app    

from app import models
