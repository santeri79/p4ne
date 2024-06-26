from flask import Flask, jsonify, render_template
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return """n order to connect to a server, the client will first have to resolve the servername 
              to an IP address - the location on the Internet where the server resides. Thus, in order for your 
             web server to be reachable, it is necessary that the servername be in DNS.

            If you don't know how to do this, you'll need to contact your network administrator, or Internet 
            service provider, to perform this step for you.

            More than one hostname may point to the same IP address, and more than one IP address can be 
            attached to the same physical server. Thus, you can run more than one web site on the same 
            physical server, using a feature called virtual hosts.
        """

if __name__ == '__main__':
    app.run(debug=True)