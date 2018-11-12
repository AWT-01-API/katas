from src.Angelica.kata_rest.RequestManager import RequestManager
from src.Angelica.kata_rest.Constans import URL_BASE

class Projects:

    def create_project(self, data):
        res = RequestManager.post(URL_BASE + '/projects',data)
        return res

    def delete_project(self, id):
        res = RequestManager.delete(URL_BASE + '/projects/' + str(id))
        return res
