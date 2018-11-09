import requests
import json

class Requests:

    def __init__(self):
        self.username = 'adrian.rojas@fundacion-jala.org'
        self.password = 'todoly12'
        self.token = "9db43079dc144688a3bc1b2320cd2688"

    def set_url(self, endpoint):
        return "https://todo.ly/api/" + endpoint + ".json"

    def create_user(self, email, full_name, password):
        url = self.set_url("user")
        data = {
            "Email": email,
            "FullName": full_name,
            "Password": password
        }
        r = requests.post(url, json.dumps(data))
        return r

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

    def edit_project(self, project_id, new_project_name = None, new_icon_no = None):
        url = self.set_url("projects/"+project_id)
        data = {
            "Content": new_project_name,
            "Icon": new_icon_no
        }
        r = requests.put(url, json.dumps(data), auth=(self.username, self.password))
        return r

    def delete_project(self, project_id):
        url = self.set_url("projects/"+project_id)
        r = requests.delete(url, auth=(self.username, self.password))
        return r
    def create_task(self, content):
        url = self.set_url("items")
        data = {
            "Content": content
        }
        r = requests.post(url, json.dumps(content), auth=(self.username, self.password))
        return r
    def edit_task(self, task_id, content):
        url = self.set_url("items/"+task_id)
        data = {
            "Content": content
        }
        r = requests.put(url, json.dumps(content), auth=(self.username, self.password))
        return r

    def delete_task(self, task_id):
        url = self.set_url("items/"+task_id)
        r = requests.delete(url, auth=(self.username, self.password))
        return r

    # def delete_trash(self):


req = Requests()
print req.create_user("pepe1234@gmail.com", "Pepe", "DonPepe123").text
