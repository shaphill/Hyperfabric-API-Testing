import requests
import json
from pprint import pprint

token = os.environ['AUTH_TOKEN']
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
}

url = "https://hyperfabric.cisco.com/api/v1/fabrics/Python-Fabric/connections"

payload = {
  "connections": [
    {
      "local": {
        "portName": "Ethernet1_31",
        "nodeName": "node-leaf0"
      },
      "remote": {
        "portName": "Ethernet1_1",
        "nodeName": "node-spine0"
      }
    },
    {
      "local": {
        "portName": "Ethernet1_31",
        "nodeName": "node-leaf1"
      },
      "remote": {
        "portName": "Ethernet1_2",
        "nodeName": "node-spine0"
      }
    },
    {
      "local": {
        "portName": "Ethernet1_32",
        "nodeName": "node-leaf0"
      },
      "remote": {
        "portName": "Ethernet1_1",
        "nodeName": "node-spine1"
      }
    },
    {
      "local": {
        "portName": "Ethernet1_32",
        "nodeName": "node-leaf1"
      },
      "remote": {
        "portName": "Ethernet1_2",
        "nodeName": "node-spine1"
      }
    }
  ]
}

response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
pprint(response.json())
