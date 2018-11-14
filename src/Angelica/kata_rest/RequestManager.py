# importing the requests library
import configparser
import requests


class RequestManager:

    def __init__(self):
        self.property = "config.properties"
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.user = self.config[self.property]['API_USER']
        self.password = self.config[self.property]['API_KEY']
        pass

    def get_endpoint(self, link):
        # api-endpoint
        return self.config[self.property]['URL_BASE'] + link + '.json'

    def post(self, link, body):
        request = requests.post(self.get_endpoint(link), body, auth=(self.user, self.password))
        return request.status_code

    def get(self, link):

        request = requests.get(self.get_endpoint(link), auth=(self.user, self.password))
        return request.status_code

    def delete(self, link):
        request = requests.delete(self.get_endpoint(link), auth=(self.user, self.password))
        return request.status_code
