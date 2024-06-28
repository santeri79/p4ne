
import requests
from flask import Flask, jsonify


USER= "restapi"
PASSWORD = "j0sg1280-7@"


headers = {
    "accept" : "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
url = "https://10.31.70.209/restconf/data/Cisco-IOS-XE-process-memory-oper:memory-usage-processes"

r = requests.get(url, headers=headers, auth=(USER, PASSWORD), verify=False)
p = r.json()


k = p["Cisco-IOS-XE-process-memory-oper:memory-usage-processes"]["memory-usage-process"]


app = Flask(__name__)
def sort_func(s):
    return int(s['allocated-memory'])

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
            return jsonify(n)

if __name__ == '__main__':


    n = sorted(k, key=sort_func,reverse=True)[0:10]


    app.run(debug=True)


