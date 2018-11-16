# importing the requests library
import requests
from src.Angelica.kata_rest.cfg.reader_cfg import Reader

class RequestManager:

    def __init__(self):
        read = Reader()
        self.user = read.get_val('API_USER')
        print (self.user)
        self.password = read.get_val('API_KEY')
        print (self.user)

    def get_endpoint(self, link):
        read = Reader()
        # api-endpoint
        self.url = read.get_val('URL_BASE')
        return self.url + link + '.json'

    def post(self, link, body):
        request = requests.post(link, body, auth=(self.user, self.password))
        return request.status_code

    def get(self, link):

        request = requests.get(self.get_endpoint(link), auth=(self.user, self.password))
        return request.status_code

    def delete(self, link):
        request = requests.delete(self.get_endpoint(link), auth=(self.user, self.password))
        return request.status_code
