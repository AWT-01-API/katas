import unittest
from src.kevinsanchez.python_request.RequestManager import RequestManager

class TestRequestManager(unittest.TestCase):

    def setUp(self):
        self.request_manager = RequestManager()

    def test_post(self):
        body = {'Content': 'testApi'}
        response = self.request_manager.post('/project', body)
        self.assertEqual(200, response.status_code)

    def test_get(self):
        project_id = '3752200'
        response = self.request_manager.get('/project/'+project_id)
        self.assertEqual(200, response.status_code)

    def test_delete(self):
        response = self.request_manager.delete('/project/' + project_id)
        self.assertEqual(200, response.status_code)