import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import config as config

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY
app.config["GITHUB_OAUTH_CLIENT_ID"] = config.GITHUB_OAUTH_CLIENT_ID
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = config.GITHUB_OAUTH_CLIENT_SECRET
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")


import views
