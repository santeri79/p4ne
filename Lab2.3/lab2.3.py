#10.31.70.208

import ansible
import glob
import paramiko
import time

USER= "av.dobrynin"
PASSWORD = "q1q1q1"
TIMEOUT = 2
BUF_SIZE = 100*1024

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect("10.31.70.208", username=USER, password=PASSWORD, look_for_keys=False, allow_agent=False)
session=ssh_connection.invoke_shell()

session.send("ansible-playbook -i inventory.ini set.yml\n")

time.sleep(TIMEOUT)

while BUF_SIZE != 0:
    out = session.recv(BUF_SIZE)
    m = out.decode()
    print(m)