import os

from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config as config


app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY
app.config["GITHUB_OAUTH_CLIENT_ID"] = config.GITHUB_OAUTH_CLIENT_ID
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = config.GITHUB_OAUTH_CLIENT_SECRET
app_path = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + app_path + '/crud.db'

github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


import views
