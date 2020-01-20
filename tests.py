import os
import unittest
from unittest.mock import MagicMock, patch

from app import app, db, app_path
from models import User, Profile


# def create_test_profile():
#     profile = Profile(user_id=1)
#     db.session.add(profile)
#     db.session.commit()


@patch("views.get_github_userid", MagicMock(return_value=10))
@patch("views.is_authorised", MagicMock(return_value=True))
class TestCrudApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config["DEBUG"] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app_path + '/test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_it_loads_ok(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_is_created_with_github_id(self):
        user = User.query.first()
        self.assertIsNone(user)

        response = self.app.get('/')
        user = User.query.first()
        self.assertIsNotNone(user)
        self.assertTrue(user.github_id, 10)

    def test_shows_correct_html_when_no_user_profile_created(self):
        html = str(self.app.get('/').data)
        #probably a better way to check
        self.assertTrue('Create Profile' in html)
        self.assertTrue('id="name"' not in html)

    def test_can_create_a_profile(self):
        profiles = Profile.query.all()
        self.assertEqual(len(profiles), 0)

        response = self.app.post('/profile', data={'user_id':1})
        profiles = Profile.query.all()
        self.assertEqual(len(profiles), 1)

    def test_shows_profile_when_user_has_one(self):
        response = self.app.get('/')
        print(response)
        profile = Profile(user_id=1)
        db.session.add(profile)
        db.session.commit()
        html = str(self.app.get('/').data)
        self.assertTrue('Create Profile' not in html)
        self.assertTrue('id="name"' in html)


if __name__ == '__main__':
    unittest.main()
