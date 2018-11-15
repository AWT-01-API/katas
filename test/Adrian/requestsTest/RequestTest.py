from unittest import TestCase
from src.Adrian.todoly.API.TodoLyRequest import TodoLyRequest
import datetime


class RequestTet(TestCase):

    def setUp(self):
        self.requests = TodoLyRequest()

    def test_create_user(self):
        r = self.requests.create_user("pepe1234@gmail.com", "Pepe Grillo", "password")
        self.assertEqual("<Response [200]>", str(r))

    def test_get_projects(self):
        r = self.requests.get_projects()
        self.assertEqual("<Response [200]>", str(r))

    def test_create_project(self):
        r = self.requests.create_project("New Project" + str(datetime.datetime.now()), "3")
        self.assertEqual("<Response [200]>", str(r))

    def test_edit_project(self):
        r = self.requests.edit_project(" project_id", "new_project_name" + str(datetime.datetime.now()), "2")
        self.assertEqual("<Response [500]>", str(r))

    def test_delete_project(self):
        r = self.requests.delete_project("project_id")
        self.assertEqual("<Response [500]>", str(r))

    def test_create_task(self):
        r = self.requests.create_task("content")
        self.assertEqual("<Response [200]>", str(r))

    def test_edit_task(self):
        r = self.requests.edit_task("task_id", "content")
        self.assertEqual("<Response [500]>", str(r))

    def test_delete_task(self):
        r = self.requests.delete_task("task_id")
        self.assertEqual("<Response [500]>", str(r))

    def test_create_project_create_task_inside_assert_delete_both(self):
        # TODO test
        # Create new project add task, check if task exists, check if its undone,
        # set as finished, delete project"
        r = self.requests.create_project("New Project" + str(datetime.datetime.now()), "3")
        self.assertEqual("<Response [200]>", str(r))
