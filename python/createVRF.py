import requests
import json
from pprint import pprint

token = ""

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
}

url = "https://hyperfabric.cisco.com/api/v1/fabrics/Python-Fabric/vrfs"

payload = {
  "vrfs": [
    {
      "name": "Vrf-example",
      "enabled": True
    },
  ]
}

response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
pprint(response.json())

