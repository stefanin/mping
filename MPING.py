#!/usr/bin/python3
#pip3 install multiping
# thanks https://github.com/romana/multi-ping
# mping rel 0.1.2
from mpingLIB import *
import socket


if __name__ == '__main__':
    if len(sys.argv)==2:
        network = sys.argv[1]
        parametro=''
    else:
        eseguibile, network, parametro = sys.argv
    try:
        #network = sys.argv[1]
        ipup=ipdown=0
        for addr, rtime in mping(network).items():
            hostname=''
            if rtime==999.9:
                rtime='down'
                ipdown=ipdown+1
            else:
                ipup=ipup+1
            if parametro=='-n':
                try:
                    hostname=socket.gethostbyaddr(str(ipaddress.IPv4Address(addr)))[0]
                except:
                    hostname=''    

            
            print( str(ipaddress.IPv4Address(addr)), rtime, hostname  )
        print('\nip up=%i down=%i' % (ipup,ipdown))
    except:
      print ('type mping x.x.x.x/x or mping x.x.x.x/x -n for dns name resolution')
    print('\nMPING rel 0.1.2 by stefanin https://github.com/stefanin/mping.git')



