import requests
import os
import json
from pprint import pprint

token = ""
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
}

url = "https://hyperfabric.cisco.com/api/v1/fabrics/Python-Fabric/nodes"

payload = {
  "nodes": [
    {
        "name": "node-leaf0",
        "description": "example fabric node leaf zero",
        "enabled": True,
        "modelName": "HF6100-60L4D",
        "roles": [ "LEAF" ],
        "labels": [ "TAG_ONE_ZERO" ]
    },
    {
        "name": "node-leaf1",
        "description": "example fabric node leaf one",
        "enabled": True,
        "modelName": "HF6100-60L4D",
        "roles": [ "LEAF" ]
    },
    {
        "name": "node-spine0",
        "description": "example fabric node spine zero",
        "enabled": True,
        "modelName": "HF6100-32D",
        "roles": [ "SPINE" ]
    },
    {
        "name": "node-spine1",
        "description": "example fabric node spine one",
        "enabled": True,
        "modelName": "HF6100-32D",
        "roles": [ "SPINE" ]
    }
  ]
}

response = requests.request('POST', url, headers=headers, data=json.dumps(payload))

pprint(response.json())