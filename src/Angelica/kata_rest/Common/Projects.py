from src.Angelica.kata_rest.RequestManager import RequestManager
import json

class Projects:


    def __init__(self):
        self.url = "https://todo.ly/api"
        pass

    def create_project(self, data):
        request = RequestManager()
        # your API key here
        url = self.url + '/projects'+'.json'
        body = json.dumps(data)
        res = request.post(url, body)
        return res.status_code

    def delete_project(self, id):
        request = RequestManager()
        res = request.delete(self.url + '/projects/' + str(id))
        return res

