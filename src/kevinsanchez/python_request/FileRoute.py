import os

"""
class to help find route of source file.
"""
class FileRoute:

    """
    method which find the route
    """
    @staticmethod
    def find_properties():
        string = os.path.dirname(os.path.abspath(__file__)) + '\\resources\\config.properties'
        return string

    @staticmethod
    def get_file_validator(file_name):
        file_schema = open(os.path.dirname(os.path.abspath(__file__))+'\\resources\\'+file_name)
        schema = file_schema.read()
        file_schema.close()
        return schema

