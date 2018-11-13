from src.Angelica.kata_rest.RequestManager import RequestManager
from src.Angelica.kata_rest.Data

class Projects:

    def create_project(self, data):
        res = RequestManager.post(Data.URL_BASE + '/projects', data)
        return res

    def delete_project(self, id):
        res = RequestManager.delete(Data.URL_BASE + '/projects/' + str(id))
        return res
