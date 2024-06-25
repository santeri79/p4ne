import pprint
import re

import requests
USER= "restapi"
PASSWORD = "j0sg1280-7@"

headers = {
    "accept" : "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
url = "https://10.31.70.209/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

r = requests.get(url, headers=headers, auth=(USER, PASSWORD), verify=False)
p = r.json()
print(type(p))
pprint.pprint(p)

for i in p["Cisco-IOS-XE-interfaces-oper:interfaces"]["interface"]:
    print(i["name"], i["v4-protocol-stats"]["in-octets"])
#print(p.get('in-octets'))


