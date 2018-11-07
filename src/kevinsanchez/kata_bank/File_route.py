import os

"""
class to help find route of source file.
"""
class File_route:

    """
    method which find the route
    """
    def find(self):
        string = os.getcwd() + '\\source_data.txt'
        return string.replace("\\", "/")
