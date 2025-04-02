import requests
import os
import json
from pprint import pprint

nodes = [
  "node-spine0",
  "node-spine1",
  "node-leaf0",
  "node-leaf1"
]

token = ""

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

payload = {
  "ports": [
      {
          "configOrigin": "CONFIG_ORIGIN_CLOUD",
          'ipv4ConfigType': 'CONFIG_TYPE_DHCP',
          'ipv6ConfigType': 'CONFIG_TYPE_DHCP',
          "proxyAddress": "http://proxy.esl.cisco.com:80"
      }
  ]
}

for node in nodes:
  url = f"https://hyperfabric.cisco.com/api/v1/fabrics/Python-Fabric/nodes/{node}/managementPorts"
  response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
  pprint(response.json())


