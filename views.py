from flask import render_template, redirect, url_for, request

from app import app, github, db
from models import User, Profile


def is_authorised():
    return github.authorized


def get_or_create_user():
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


@app.route('/')
def index():
    if not is_authorised():
        return redirect(url_for("github.login"))
    user = get_or_create_user()
    print(user)
    profile = Profile.query.filter_by(user_id=user.id).first()
    if profile:
        print(profile.user_id)
    return render_template('profile.html', profile=profile, user_id=user.id)


@app.route('/profile', methods=["POST"])
def create_profile():
    print('yesss')
    profile = Profile()
    profile.user_id = request.form.get("user_id")
    db.session.add(profile)
    db.session.commit()
    return redirect("/")


@app.route('/profile/update', methods=["POST"])
def update_profile():
    profile = Profile.query.get(request.form.get('id'))
    profile.name = request.form.get('name')
    db.session.commit()
    return redirect("/")
