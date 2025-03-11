import socket
import sys 
import os
import threading
import time
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-ip', '--ip')
parser.add_argument('-p', '--port', nargs=1)
parser.add_argument('-t', '--time')
parser.add_argument('-f', '--file')
args = parser.parse_args()

target=socket.gethostbyname(args.ip)
print("IP: " + str(target))

try:
	portMin = int(args.port[0][:args.port[0].index("-")])
	portMax = int(args.port[0][args.port[0].index("-")+1:])
except ValueError:
	portMin = int(args.port[0])
	portMax = int(args.port[0])

try:
	time_wait = float(args.time)
except TypeError:
	time_wait = 0.01

file = args.file

ports = []
try:

	res = socket.gethostbyaddr(args.ip)
	print("Hostname: " + str(res[0]))

except socket.herror:
	print("Could not find Hostname")

def connect(host, port):
	socket.setdefaulttimeout(1)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex((target, port))
	if result == 0:
		try:
			print("successful connection on port {}, service: {}".format(port,socket.getservbyport(port, 'tcp')))
			ports.append("successful connection on port {}, service: {}".format(port,socket.getservbyport(port, 'tcp')) + "\n")
		except OSError:
			print("successful connection on port {}, service: {}".format(port,"unknown"))
			ports.append("successful connection on port {}, service: {}".format(port,"unknown") + "\n")
			#global append
			#append += "successful connection on port {}, service: {}".format(port,socket.getservbyport(port, 'tcp')) + "\n"
			
	s.close()

try:
	threads = []
	for port in range(portMin, portMax + 1):
		thread = threading.Thread(target=connect, args=(target, port,))
		threads.append(thread)

	batch_size = 500
	for i in range(0, len(threads), batch_size):
		for thread in threads[i:i + batch_size]:  
			thread.start()
		for thread in threads[i:i + batch_size]:  
			thread.join()

except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()

if file is not None:
	f = open(file, "w")
	for port in ports:
		f.write(port)
	f.close()