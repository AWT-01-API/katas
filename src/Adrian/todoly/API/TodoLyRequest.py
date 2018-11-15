from src.Adrian.todoly.util.ReadCfg import ReadCfg
from src.Adrian.todoly.API.RequestManager import RequestManager
import requests
import json


class TodoLyRequest:

    def __init__(self):
        self.url = ReadCfg.get_value("url")
        self.username = ReadCfg.get_value("username")
        self.password = ReadCfg.get_value("password")
        self.token = ReadCfg.get_value("token")
        self.request = RequestManager(self.url, self.username, self.password)
        self.request.set_token(self.token)

    @staticmethod
    def set_url(endpoint):
        return ReadCfg.get_value("url") + endpoint + ".json"

    def create_user(self, email, full_name, password):
        data = {
            "Email": email,
            "FullName": full_name,
            "Password": password
        }
        return self.request.post_request("user", data)

    def get_projects(self):
        url = self.set_url("projects")
        r = requests.get(url, auth=(self.username, self.password))
        return r

    def create_project(self, project_name, icon_no):
        url = self.set_url("projects")
        data = {
            "Content": project_name,
            "Icon": icon_no
        }
        r = requests.post(url, json.dumps(data), auth=(self.username, self.password))
        return r

    def edit_project(self, project_id, new_project_name=None, new_icon_no=None):
        url = self.set_url("projects/" + project_id)
        data = {
            "Content": new_project_name,
            "Icon": new_icon_no
        }
        r = requests.put(url, json.dumps(data), auth=(self.username, self.password))
        return r

    def delete_project(self, project_id):
        url = self.set_url("projects/" + project_id)
        r = requests.delete(url, auth=(self.username, self.password))
        return r

    def get_tasks_of_project(self, project_id):
        url = self.set_url(project_id + "/items")
        r = requests.get(url, auth=(self.username, self.password))
        return r

    def get_all_tasks(self, task_id):
        url = self.set_url("/items/" + task_id)
        r = requests.get(url, auth=(self.username, self.password))
        return r

    def get_task(self, project_id):
        url = self.set_url(project_id + "/items")
        r = requests.get(url, auth=(self.username, self.password))
        return r

    def create_task(self, content):
        url = self.set_url("items")
        data = {
            "Content": content
        }
        r = requests.post(url, json.dumps(data), auth=(self.username, self.password))
        return r

    def edit_task(self, task_id, content):
        url = self.set_url("items/" + task_id)
        data = {
            "Content": content
        }
        r = requests.put(url, json.dumps(data), auth=(self.username, self.password))
        return r

    def delete_task(self, task_id):
        url = self.set_url("items/" + task_id)
        r = requests.delete(url, auth=(self.username, self.password))
        return r

    def get_task_done(self, task_id):
        url = self.set_url("items/" + task_id)
        data = {
            "Checked": "true",
        }
        r = requests.put(url, json.dumps(data), auth=(self.username, self.password))
        return r
