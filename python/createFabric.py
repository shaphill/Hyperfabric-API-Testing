import requests
import json
from pprint import pprint

token = os.environ['AUTH_TOKEN']

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
}

url = "https://hyperfabric.cisco.com/api/v1/fabrics"

payload = {
    "fabrics": [
        {
            "name": "Python-Fabric",
            "description": "Fabric created via Python",
        }
    ]
}


response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

pprint(response.json())
