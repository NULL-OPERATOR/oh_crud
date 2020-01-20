from flask import render_template, redirect, url_for

from app import app, github


@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    response = github.get("/user")
    assert resp.ok
    id = response.json()['id']

    return render_template('profile.html')


@app.route('/profile', methods=["POST"])
def create_profile():
    # moake profile on post
    return redirect("/")
