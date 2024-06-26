#!/usr/bin/env python3

import os
import sys


#names = ["Bruno", "Maria", "Joao"]
# LBYL - Look Before You Leap

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # race condition
    names = open("names.txt").readlines()
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
    
if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
    
print(names[3])