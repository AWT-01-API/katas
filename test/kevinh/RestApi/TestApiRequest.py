from src.kevinh.RestApi.ApiRequest import RequestAPI
import unittest
import json


class TestFactorial(unittest.TestCase):
    def setUp(self):
        self.api = RequestAPI()
        self.api.set_credentials('todo.ly.rest@apitest.com', 'control123')

    def test_request_get_token(self):
        url = "https://todo.ly/api/authentication/token.xml"
        request = self.api.get_request(url)
        self.assertEqual(200, request.status_code)

    def test_request_post_project(self):
        url = "https://todo.ly/api/projects.json"
        body = {"Content": "MyNewProject12-11-18", "Icon": "3"}
        request = self.api.post_request(url, json.dumps(body))
        self.assertEqual(200, request.status_code)
