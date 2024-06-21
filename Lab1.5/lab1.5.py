import glob


import glob

files = glob.glob('*.log')
print(files)
ipaddress_list = []
for i in range(len(files)):
    with open(files[i]) as f:
        for l in f:
            if l.find("ip address") != -1:
                ipaddress_list.append(l)

        f.close()

#print(*ipaddress_list, sep='\n')

my_set = set(ipaddress_list)
my_list = list(my_set)

print(*my_list, sep='\n')

s1 = "ip address "
for i in range(len(my_list)):
    print(my_list[i][len(s1):])