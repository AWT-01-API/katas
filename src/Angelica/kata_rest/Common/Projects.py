from src.Angelica.kata_rest.RequestManager import RequestManager
import configparser

class Projects:
    def __init__(self):
        self.property = "config.properties"
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.url = self.config[self.property]['URL_BASE']
        pass

    def create_project(self, data):
        url = self.url + '/projects'
        res = RequestManager.post(url, data)
        return res

    def delete_project(self, id):
        res = RequestManager.delete(self.url + '/projects/' + str(id))
        return res
