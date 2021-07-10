#!/usr/bin/env python3

import sys
import hashlib

def file_hasher(f2_line):
    f0 = sys.argv[1]
    with open(f0, "r") as newfile:
        all_content = newfile.read()
        result = hashlib.md5(all_content.encode())
        hashed = result.hexdigest()
    if hashed == f2_line: 
        return True 
        

def main():
	
    f2 = ("/root/bad-hash-of-files")

    with open(f2, "r" ) as newfile2:
        for h2 in newfile2.readlines():
            if file_hasher(h2.strip()):
                return "Hash found in database and is NOT SAFE. Please contact your system admin immediately" 
    return "File is safe. Please proceed."

print(main())
