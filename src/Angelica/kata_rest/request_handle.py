# importing the requests library
import requests
import json

# api-endpoint
URL = "https://todo.ly/api/projects.json"

proy = "test5"

# your API key here
API_USER = "anghelita@mailinator.com"
API_KEY = ""

# defining a params dict for the parameters to be sent to the API
PARAMS = {'Content':'proy', 'Icon':'4'}

param_body = json.dumps(PARAMS)

# sending get request and saving the response as response object
r = requests.post(URL, param_body, auth=(API_USER, API_KEY))

#code status
print (r.status_code)

# extracting data in json format
data = r.json()
print data
