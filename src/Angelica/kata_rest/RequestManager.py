# importing the requests library
import configparser
import requests


class RequestManager:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("/Users/angi/Desktop/kataspy/katas/src/Angelica/kata_rest/cfg/config.ini")
        self.user = self.config.get('configuration', 'API_USER')
        self.password = self.config.get('configuration', 'API_KEY')
        pass

    def get_endpoint(self, link):
        # api-endpoint
        self.url = self.config.get('configuration', 'URL_BASE')
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
