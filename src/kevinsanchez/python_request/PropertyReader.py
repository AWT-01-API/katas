import ConfigParser
from src.kevinsanchez.python_request.FileRoute import FileRoute

"""
Class to read the propertye file.
"""
class PropertyReader:

    """
    method which toget the property.
    :param option property to search/
    :return property
    """
    @staticmethod
    def get_property(option):
        config = ConfigParser.RawConfigParser()
        config.read(FileRoute.find('config.properties'))
        return config.get('Environment', option)

