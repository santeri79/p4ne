import pprint
import requests
from flask import Flask
import glob
import re


USER= "restapi"
PASSWORD = "j0sg1280-7@"


headers = {
    "accept" : "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
url = "https://10.31.70.209/restconf/data/Cisco-IOS-XE-process-memory-oper:memory-usage-processes"

r = requests.get(url, headers=headers, auth=(USER, PASSWORD), verify=False)
p = r.json()
print(type(p))
pprint.pprint(p)

for key in p:
   print(f'{key},{p[key]}', file=result.py)

for i in p["Cisco-IOS-XE-process-memory-oper:memory-usage-processes"]["memory-usage-process"]:
    print(i["name"], ":", i["allocated-memory"])

######################################################################################################
app = Flask(__name__)
def match_conf(s):
    m = re.match("^ip address ((?:[0-9]{1,3}[.]?){4}) ((?:[0-9]{1,3}[.]?){4})", s)

    if m :
        return m.group(1)

    else:
        return None

@app.route('/')
@app.route('/index')
def index():
    return """In order to connect to a server, the client will first have to resolve the servername 
              to an IP address - the location on the Internet where the server resides. Thus, in order for your 
             web server to be reachable, it is necessary that the servername be in DNS.        
        """
@app.route('/process')
def process():
            return str(p)

if __name__ == '__main__':

    n = []

    for i in files:
        with open(i) as f:
            line_list = f.readlines()
            for line in line_list:
                s1 = match_conf(line.strip())
                if s1:
                    n.append(s1)


            f.close()

    app.run(debug=True)

