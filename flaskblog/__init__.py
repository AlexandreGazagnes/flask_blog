import logging
import os
from logging import warning, debug, info
logging.basicConfig(level=logging.INFO)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# app and derivatives
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config["MAIL_SERVER"] = 'smtp.googlemail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = 'smtp.googlemail.com'
app.config['MAIL_USERNAME'] = os.environ.get("YAHOO_EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get("YAHOO_PASSWORD")
mail = Mail(app)


# blueprints
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

# for cli interface
from flaskblog.models import User, Post
