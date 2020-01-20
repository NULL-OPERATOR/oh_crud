import unittest

from app import app


class TestCrudApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_it_loads_ok(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
