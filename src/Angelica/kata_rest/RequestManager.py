# importing the requests library
from src.Angelica.kata_rest.Constans import API_KEY, API_USER, URL_BASE
import requests
import json


class RequestManager:

    def __init__(self):
        pass

    def get_endpoint(self, link):
        # api-endpoint
        return URL_BASE + link + '.json'

    def post(self, link, body):
        body = json.dumps(body)
        request = requests.post(self.get_endpoint(link), body, auth=(API_USER, API_KEY))
        return request.status_code

    def get(self, link):
        request = requests.get(self.get_endpoint(link), auth=(API_USER, API_KEY))
        return request.status_code

    def delete(self, link):
        request = requests.delete(self.get_endpoint(link), auth=(API_USER, API_KEY))
        return request.status_code
