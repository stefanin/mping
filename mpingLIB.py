#!/usr/bin/python3
#pip3 install multiping
# thanks https://github.com/romana/multi-ping
# mpingLIB mping rel 0.1.3
# mpingLIB mping rel 4.1.9 return IPv4 string
import sys
from multiping import MultiPing
import ipaddress 

def mping(network, ipInt=True): #network= x.x.x.x/x if ipInt like Truereturn dict{ip(int), time(float)}
    '''
    network= x.x.x.x/x 
    if ipInt == True return dict{IPv4(int), time(float)}
    if ipInt == False return dict{IPv4(string), time(float)}
    '''
    ip_per_scan=''
    if network[-2:]=='32':
        ip_per_scan=network[:-3]
    else:    
        try:
            for x in ipaddress.ip_network(network).hosts():
                ip_per_scan=ip_per_scan+' '+str(x)
        except:
            print('network %s do not conform' % network)
            #break

    mp = MultiPing(ip_per_scan.split())
    mp.send()
    responses, no_responses = mp.receive(1)
    if no_responses:
        for addr in no_responses:
            responses[addr]=1
        
    ipscan_tmp={}
    for addr, rtt in responses.items():
        ipscan_tmp[int(ipaddress.IPv4Address(addr))]=round((rtt*1000),2)

    ipscan={}
    for addr in sorted(ipscan_tmp.keys()): #ordina per ip adress
        if ipInt:
            ipscan[addr]=ipscan_tmp[addr]
        else:
            ipscan[ipaddress.ip_address(addr).__str__()]=ipscan_tmp[addr]

    return ipscan



