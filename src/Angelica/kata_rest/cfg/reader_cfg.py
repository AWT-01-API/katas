import configparser
import os

"""
class to help find value.
"""
class Reader:

    def get_path(self):
        string_path = os.getcwd() + '\\cfg\\config.ini'
        path = string_path.replace("\\", "/")
        return path

    def get_val(self,key):
        self.config = configparser.ConfigParser()
        self.config.sections()
        path = self.get_path()
        self.config.read(path)
        self.val = self.config.get('configuration', key)
        return self.val
