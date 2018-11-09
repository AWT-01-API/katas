import requests
import json


class RequestManager:

    def __init__(self):
        self.base_url = 'https://todo.ly/api'
        self.header = {'X-TrackerToken': 'ea41d94388244b628a773051ff97d0a4',
                       'Content-Type': 'application/json',
                       'Authorization': 'Basic a2V2aW4uc2FuY2hlenBlZXBAZ21haWwuY29tOjcyNDk1NDMxVEFOSUF0ayE='}

    def complete_url(self, endpoint):
        return self.base_url+endpoint+'.json'

    def post(self, end_point, body):
        body = json.dumps(body)
        request = requests.post(self.complete_url(end_point),
                                headers=self.header,
                                data=body)
        return request

    def get(self, end_point):
        request = requests.get(self.complete_url(end_point),
                               headers=self.header)
        return request

    def delete(self, end_point):
        request = requests.delete(self.complete_url(end_point),
                                  headers=self.header)
        return request

    def get_a_project_(self, id_project):
        request_type = requests.get('https://todo.ly/api/projects/' + str(id_project) + '.json', headers=self.header)
        return request_type

    def get_all_projects(self):
        request_type = requests.get('https://todo.ly/api/projects.json', headers=self.header)
        return request_type

    def create_project(self, data_project):
        request_type = requests.post('https://todo.ly/api/projects.json',
                                     headers=self.header,
                                     data=json.dumps(data_project))
        return request_type

    def update_project(self, data_project):
        request_type = requests.post('https://todo.ly/api/projects/' + data_project['Id'] + '.json',
                                     headers=self.header,
                                     data=json.dumps(data_project))
        return request_type

    def delete_project(self, id_project):
        request_type = requests.delete('https://todo.ly/api/projects/' + str(id_project) + '.json', headers=self.header)
        return request_type

