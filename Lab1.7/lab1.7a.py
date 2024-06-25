import pprint
import socket
#https://binlist.net/
headers = {"Accept-Version": "3"}
url = "https://lookup.binlist.net/45717360"
r = requests.get(url, headers=headers)
r.status.code
r.content
r.text
dict3 = r.json()
pprint.pprint(dict3)