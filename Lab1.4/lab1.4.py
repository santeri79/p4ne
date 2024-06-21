from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        net = random.randint(0X0b000000, 0xdf000000)
        mask = random.randint(8,24)
        IPv4Network.__init__(self, (net, mask), strict=False)

address_list = []

for i in range(0, 51):
    net1 = IPv4RandomNetwork()
    address_list.append(net1)






