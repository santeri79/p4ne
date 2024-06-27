import glob
import re
import ipaddress

files = glob.glob('*.log')
print(files)

def match_func(s):
    m = re.match("^ip address ((?:[0-9]{1,3}[.]?){4}) ((?:[0-9]{1,3}[.]?){4})", s)
    if m:
        return ipaddress.IPv4Interface((m.group(1), m.group(2)))
    else:
        return None

for i in files:
    with open(i) as f:
        line_list = f.readlines()
        for line in line_list:
            s1 = match_func(line.strip())
            if s1:
                print(s1)

        f.close()





