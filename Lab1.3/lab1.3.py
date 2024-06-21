from pysnmp.hlapi import *

snmp_name = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_interfaces = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result_1 = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.209',161)),
    ContextData(),
    ObjectType(snmp_name),
)


for answer in result_1:
    for s in answer[3]:
       print(s)

result_2 = nextCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.209',161)),
    ContextData(),
    ObjectType(snmp_interfaces),
    lexicographicMode=False
)

for answer in result_2:
    for s in answer[3]:
       print(s)