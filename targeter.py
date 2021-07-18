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

def get_unwawnted(potential_targets):
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

potential_targets = (get_targets())
get_unwawnted(potential_targets)
