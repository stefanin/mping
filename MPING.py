#!/usr/bin/python3
#pip3 install multiping
# thanks https://github.com/romana/multi-ping
# mping rel 0.1.1
from mpingLIB import *


if __name__ == '__main__':
    try:
        network = sys.argv[1]
        ipup=ipdown=0
        for addr, rtime in mping(network).items():
            if rtime==999.9:
                rtime='down'
                ipdown=ipdown+1
            else:
                ipup=ipup+1

            print( str(ipaddress.IPv4Address(addr)), rtime)
        print('\nip up=%i down=%i' % (ipup,ipdown))
    except:
      print ('type mping x.x.x.x/x')
    print('\nMPING rel 0.1.1 by stefanin https://github.com/stefanin/mping.git')



