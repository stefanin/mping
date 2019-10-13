#!/usr/bin/python3
#pip3 install multiping
# thanks https://github.com/romana/multi-ping
import sys
from multiping import MultiPing
import ipaddress 

def mping(network): #network= x.x.x.x/x return dict{ip(int), time(float)}
        ip_per_scan=''
        for x in ipaddress.ip_network(network).hosts():
            ip_per_scan=ip_per_scan+' '+str(x)

        mp = MultiPing(ip_per_scan.split())
        mp.send()
        responses, no_responses = mp.receive(1)

        if no_responses:
            for addr in no_responses:
                responses[addr]=0.9999
            
        ipscan_tmp={}
        for addr, rtt in responses.items():
            ipscan_tmp[int(ipaddress.IPv4Address(addr))]=round((rtt*1000),2)

        ipscan={}
        for addr in sorted(ipscan_tmp.keys()): #ordina per ip adress
            ipscan[addr]=ipscan_tmp[addr]
        return ipscan

if __name__ == '__main__':
    try:
        network = sys.argv[1]
        for addr, rtime in mping(network).items():
            if rtime==999.9:
                rtime='down'
            print( str(ipaddress.IPv4Address(addr)), rtime)
    except :
      print ('mping re.0.1 type mping x.x.x.x/x')



