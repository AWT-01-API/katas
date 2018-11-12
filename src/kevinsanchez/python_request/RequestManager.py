import requests
import json

"""
class to manage requests.
"""
class RequestManager:

    """
    constructor for header.
    """
    def __init__(self):
        self.base_url = 'https://todo.ly/api'
        self.header = {'X-TrackerToken': '8cabd12b477044edabc96378787fc9cd',
                       'Content-Type': 'application/json',
                       'Authorization': 'Basic a2V2aW4uc2FuY2hlenBlZXBAZ21haWwuY29tOjcyNDk1NDMxVEFOSUF0ayE='}

    """
    creates url for requests.
    :param endpoint to construct url.
    :return url.
    """
    def complete_url(self, endpoint):
        return self.base_url+endpoint+'.json'

    """
    post requests.
    :param endpoint for page.
    :body to be send to url.
    :return response.
    """
    def post(self, endpoint, body):
        body = json.dumps(body)
        request = requests.post(self.complete_url(endpoint),
                                headers=self.header,
                                data=body)
        return request

    """
    get requests.
    :param endpoint for page.
    :return response.
    """
    def get(self, endpoint):
        request = requests.get(self.complete_url(endpoint),
                               headers=self.header)
        return request

    """
    delete request.
    :param endpoint for page.
    :return response.
    """
    def delete(self, endpoint):
        request = requests.delete(self.complete_url(endpoint),
                                  headers=self.header)
        return request
