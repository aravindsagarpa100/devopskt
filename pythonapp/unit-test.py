import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_cat_route(self):
        response = self.app.get('/cat')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'You Chose CAT')

    def test_dog_route(self):
        response = self.app.get('/dog')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'You Chose DOG')

    def test_wrong_route(self):
        response = self.app.get('/wrong')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Choose CAT or DOG')

if __name__ == '__main__':
    unittest.main()
