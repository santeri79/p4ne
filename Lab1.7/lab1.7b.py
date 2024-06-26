import paramiko
import time
import pprint
import re

BUF_SIZE = 100*1024
TIMEOUT = 2
USER= "restapi"
PASSWORD = "j0sg1280-7@"

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect("10.31.70.209", username=USER, password=PASSWORD, look_for_keys=False, allow_agent=False)
session=ssh_connection.invoke_shell()

session.send("terminal length 0\n")
session.send("show interfaces\n")
time.sleep(TIMEOUT)
out = session.recv(BUF_SIZE)

m = out.decode()
print(m)

def match_interface(s):
    m = re.match("^GigabitEthernet((?:[0-9]{1}))", s)
    n = re.match("^Loopback((?:[0-9]{1}))", s)
    if m:
        return m.group(0)
    elif n:
        return n.group(0)
    else:
        return None




