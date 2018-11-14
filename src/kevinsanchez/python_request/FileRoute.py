import os

"""
class to help find route of source file.
"""
class FileRoute:

    """
    method which find the route
    """
    def find(self):
        string = os.getcwd() + '\\config.properties'
        return string.replace("\\", "/")
