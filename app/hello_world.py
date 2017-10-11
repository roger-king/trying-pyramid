import unittest
from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setup(self):
        self.config = testing.setUp()
    
    def tearDown(self):
        testing.tearDown()
    
    def test_hello_world(self):
        from app import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
