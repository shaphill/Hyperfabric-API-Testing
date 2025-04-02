import requests
import json
from pprint import pprint

token = os.environ['AUTH_TOKEN']

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
}

url = "https://hyperfabric.cisco.com/api/v1/fabrics/Python-Fabric/vnis"


payload = {
"vnis": [
    {
      "name": "net1",
      "enabled": True,
      "svis": [
        {
          "ipv4Addresses": [ "192.168.1.254/24" ],
          "enabled": True
        }
      ]
    } 
  ]
}

response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
pprint(response.json())