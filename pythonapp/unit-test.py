import unittest
from flask import Flask
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
        self.assertEqual(response.data.decode('utf-8'), 'You have to choose either CAT or DOG')

    def test_login_cat(self):
        response = self.app.post('/login', data={'nm': 'cat'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/cat')

    def test_login_dog(self):
        response = self.app.post('/login', data={'nm': 'dog'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/dog')

    def test_login_wrong(self):
        response = self.app.post('/login', data={'nm': 'cow'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/wrong')

if __name__ == '__main__':
    unittest.main()
