#!/usr/bin/env python3

import sys
import subprocess

from scapy.all import ARP, Ether, srp

def worm_spread():

    target_ip = "192.168.56.111/24"

    # create ARP packet
    arp = ARP(pdst=target_ip)

    # create the Ether broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # stack them
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, to be filled in the upcoming loop
    clients = []

    for sent, received in result:
    # for each response, append ip 
        clients.append(received.psrc)
    return clients
print(worm_spread())


def nc_listener():
    nc_setup=subprocess.run(["nc", "-lp", "1337"])
    return nc_setup
print(nc_listener())


