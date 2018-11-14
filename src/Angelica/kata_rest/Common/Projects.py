from src.Angelica.kata_rest.RequestManager import RequestManager
import configparser

class Projects:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("/Users/angi/Desktop/kataspy/katas/src/Angelica/kata_rest/cfg/config.ini")
        self.url = self.config.get('configuration','URL_BASE')
        pass

    def create_project(self, data):
        request = RequestManager()
        url = self.url + '/projects'
        print(url)
        res = request.post(url, data)
        return res

    def delete_project(self, id):
        request = RequestManager()
        res = request.delete(self.url + '/projects/' + str(id))
        return res

    def config_section_map(self,section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
