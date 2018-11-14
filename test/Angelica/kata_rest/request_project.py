import unittest
import json
from src.Angelica.kata_rest.Common.Projects import Projects

class ProjectTest(unittest.TestCase):

    def test_create_project(self):
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'Content': 'proy', 'Icon': '4'}
        body = json.dumps(PARAMS)
        proy = Projects()
        status_code = proy.create_project(body)
        self.assertEqual(200, status_code)
