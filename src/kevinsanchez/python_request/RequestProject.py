import requests
import json


class RequestProject:
    def __init__(self):
        self.header = {'X-TrackerToken': 'ea41d94388244b628a773051ff97d0a4',
                          'Content-Type': 'application/json',
                          'Authorization': 'Basic a2V2aW4uc2FuY2hlenBlZXBAZ21haWwuY29tOjcyNDk1NDMxVEFOSUF0ayE='}

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
        request_type = requests.post('https://todo.ly/api/projects/'+data_project['Id']+'.json',
                                     headers=self.header,
                                     data=json.dumps(data_project))
        return request_type

    def delete_project(self, id_project):
        request_type = requests.delete('https://todo.ly/api/projects/' + str(id_project) + '.json', headers=self.header)
        return request_type

r = Request()
print (r.delete_project(3752269))
#print (request_type.json()['Id'])
#print (request_type.json()['Content'])
#print(request_type.status_code)