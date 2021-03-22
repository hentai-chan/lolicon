import unittest

from src.lolicon.utils import RequestHandler

class TestRequestHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.handler = RequestHandler()

    def test_get(self):
        api = "https://jsonplaceholder.typicode.com/todos/1"
        response = self.handler.get(url=api)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        api = "https://jsonplaceholder.typicode.com/posts"
        response = self.handler.post(url=api, payload={ 'Message': "Hello, World!" })
        self.assertEqual(response.status_code, 201)
