import os
import unittest
from unittest.mock import MagicMock, patch

from app import app, db, app_path
from models import User, Profile


def create_test_profile():
    profile = Profile(user_id=1)
    db.session.add(profile)
    db.session.commit()


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


if __name__ == '__main__':
    unittest.main()
