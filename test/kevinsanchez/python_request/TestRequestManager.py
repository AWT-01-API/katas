import unittest
import jsonschema
import simplejson as json
from src.kevinsanchez.python_request.RequestManager import RequestManager

"""
class for test.
"""
class TestRequestManager(unittest.TestCase):

    """
    set up for test.
    """
    def setUp(self):
        self.request_manager = RequestManager()
        file = open('schema-project.json')
        schema_data = file.read()
        file.close()
        self.schema_project = json.loads(schema_data)
        file = open('schema-item.json')
        schema_data = file.read()
        file.close()
        self.schema_item = json.loads(schema_data)

    """
    test post request for project and item.
    """
    def test_post(self):
        # post for project
        body = {'Content': 'Test Project'}
        response = self.request_manager.post('/projects', body)
        json_obj_project = response.json()
        jsonschema.validate(json_obj_project, self.schema_project)
        self.assertEqual(200, response.status_code)
        # post for item
        body = {'Content': 'Test Item',
                'ProjectId': response.json()['Id']}
        response_item = self.request_manager.post('/items', body)
        json_obj_item = response_item.json()
        jsonschema.validate(json_obj_item, self.schema_item)
        self.assertEqual(200, response_item.status_code)

    """
    test get request for project and item.
    """
    def test_get(self):
        # get for project
        # create project to get it with the id
        body = {'Content': 'Test Project to get'}
        project_id = self.request_manager.post('/projects', body).json()['Id']
        response = self.request_manager.get('/projects/' + str(project_id))
        json_obj_project = response.json()
        jsonschema.validate(json_obj_project, self.schema_project)
        self.assertEqual(200, response.status_code)

        # get for item
        # create a item to get it with the id
        body_item = {'Content': 'Test Item',
                     'ProjectId': response.json()['Id']}
        item_id = self.request_manager.post('/items', body_item).json()['Id']
        response_item = self.request_manager.get('/items/' + str(item_id))
        json_obj_item = response_item.json()
        jsonschema.validate(json_obj_item, self.schema_item)
        self.assertEqual(200, response_item.status_code)

    """
    test delete request for project and item.
    """
    def test_delete(self):
        # create project to delete
        body = {'Content': 'Test Project to delete'}
        project_id = self.request_manager.post('/projects', body).json()['Id']

        # create item to delete
        body_item = {'Content': 'Test Item to delete',
                     'ProjectId': project_id}
        item_id = self.request_manager.post('/items', body_item).json()['Id']

        # delete item
        response_item = self.request_manager.delete('/items/' + str(item_id))
        json_obj_item = response_item.json()
        jsonschema.validate(json_obj_item, self.schema_item)
        self.assertEqual(200, response_item.status_code)

        # delete project
        response = self.request_manager.delete('/projects/' + str(project_id))
        json_obj_project = response.json()
        jsonschema.validate(json_obj_project, self.schema_project)
        self.assertEqual(200, response.status_code)

