import stashy
import requests
from requests.auth import HTTPBasicAuth
import json
import sys




def to_bitbucket(username, password, project_name, project_key):
    bitbucket = stashy.connect("http://localhost:7990/", username, password)
    bitbucket.projects.create(project_key, project_name)
    
def get_projects_from_jira():
    url = "https://your-domain.atlassian.com/rest/api/3/project"
    auth = HTTPBasicAuth("email@example.com", "<api_token>")
    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
    url,
    headers=headers,
    auth=auth
    )
    if(response.status_code == 200):
        return []
    
    else:
        print(response.status_code)
        print("Error occured while getting projects from jira")
        return projects["ABC", "XYZ"]
    




if(len(sys.argv)<3):
    print("please enter username and password of authorized user for example main.py testusername testpassword")
    sys.exit()

username = sys.argv[1]
password = sys.argv[2]

projects = get_projects_from_jira()

to_bitbucket(username,password,"ABC")
