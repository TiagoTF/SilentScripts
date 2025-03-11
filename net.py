import os
import socket
import sys


os.system("bash ipscan.sh " + sys.argv[1])

ips = open("ficheiro.txt", "r").readlines()

for ip in ips:
	ip = ip.rstrip('\n')
	try:
		res = socket.gethostbyaddr(ip)
		print("IP: " + str(ip) + " Hostname: " + str(res[0]))
	except socket.herror:
		print(ip)


