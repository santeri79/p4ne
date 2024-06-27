from flask import Flask, jsonify, render_template
import sys
import glob
import re
import ipaddress

app = Flask(__name__)
def match_conf(s):
    m = re.match("^ip address ((?:[0-9]{1,3}[.]?){4}) ((?:[0-9]{1,3}[.]?){4})", s)

    if m :
        return m.group(1)

    else:
        return None
def match_host(s):
    m = re.match("^hostname (.+)", s)
    m1 = re.match("^sysname (.+)", s)
    if m :
        return m.group(1)
    elif m1:
        return m1.group(1)
    else:
        return None
@app.route('/')
@app.route('/index')
def index():
    return """In order to connect to a server, the client will first have to resolve the servername 
              to an IP address - the location on the Internet where the server resides. Thus, in order for your 
             web server to be reachable, it is necessary that the servername be in DNS.

            If you don't know how to do this, you'll need to contact your network administrator, or Internet 
            service provider, to perform this step for you.

            More than one hostname may point to the same IP address, and more than one IP address can be 
            attached to the same physical server. Thus, you can run more than one web site on the same 
            physical server, using a feature called virtual hosts.
        """
@app.route('/config')
def config():
            return str(n)
@app.route('/hostname')
def hostname():
            return str(p)


if __name__ == '__main__':

    n = []
    p = []
    files = glob.glob('*.log')


    for i in files:
        with open(i) as f:
            line_list = f.readlines()
            for line in line_list:
                s1 = match_conf(line.strip())
                s2 = match_host(line.strip())
                if s1:
                    n.append(s1)
                elif s2:
                    p.append(s2)

            f.close()

    app.run(debug=True)