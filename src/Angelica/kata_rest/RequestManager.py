# importing the requests library
from src.Angelica.kata_rest.Data
import requests
import json


class RequestManager:

    def get_endpoint(self, link):
        # api-endpoint
        return Data.URL_BASE + link + '.json'

    def post(self, link, body):
        body = json.dumps(body)
        request = requests.post(self.get_endpoint(link), body, auth=(Data.API_USER, Data.API_KEY))
        return request.status_code

    def get(self, link):
        request = requests.get(self.get_endpoint(link), auth=(Data.API_USER, Data.API_KEY))
        return request.status_code

    def delete(self, link):
        request = requests.delete(self.get_endpoint(link), auth=(Data.API_USER, Data.API_KEY))
        return request.status_code
