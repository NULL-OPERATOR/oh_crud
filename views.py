from flask import render_template, redirect, url_for

from app import app, github, db
from models import User, Profile


@app.route('/')
def index():
    if not is_authorised():
        return redirect(url_for("github.login"))
    user = get_or_create_user()
    print(user)
    return render_template('profile.html')



@app.route('/profile', methods=["POST"])
def create_profile():
    # moake profile on post
    return redirect("/")


def is_authorised():
    return github.authorized


def get_or_create_user():
    print('get_or_create_user')
    github_id = get_github_userid()
    print(github_id)
    user = User.query.filter_by(github_id=github_id).first()
    if not user:
        user = User()
        user.github_id = github_id
        db.session.add(user)
        db.session.commit()
    return user


def get_github_userid():
    response = github.get('/user')
    assert response.ok
    return response.json()['id']
