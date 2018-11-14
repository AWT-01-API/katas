import os

"""
class to help find route of source file.
"""
class FileRoute:

    """
    method which find the route
    """
    @staticmethod
    def find(route):
        string = (os.path.dirname(__file__)+'\\'+route)
        return string
