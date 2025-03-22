from pyfiglet import figlet_format
from termcolor import colored
import os
import sys
import time

print((colored(figlet_format("SilentScripts"), color="red")))

print("Author: Tiago Ferreira and Diogo Ribeiro\n")

def RunPortScan():
	ip = input("IP: ")
	ports = input("Ports: ")
	file = input("File(Press enter to skip): ") 
	timer = input("Timer(Press enter to skip): ")
	ArgsToAdd = ""
	if file:
		ArgsToAdd += f" -f {file}"
	if timer:
		ArgsToAdd += f" -t {timer}"
	os.system("clear")
	os.system(f"python3 Port.py -ip {ip} -p {ports}{ArgsToAdd}")
	print("")

def WebBruteforce():
	url = input("URL:")
	os.system("clear")
	os.system(f"python3 WebBruteforce.py -url {url}")
	print("")

def DirFinder():
	url = input("URL:")
	worldlist = input("Wordlist(enter to skip):")
	appendwordlist = ""
	if worldlist:
		appendwordlist += f" -w {worldlist}"
	os.system("clear")
	os.system(f"python3 dirbuster.py -url {url}{appendwordlist}")
	print("")

def SSHBruteforce():
	user = input("User:")
	ip = input("IP:")
	file = input("File(enter to skip):")
	addfile = ""
	if file:
		addfile = f" -f {file}"
	os.system("clear")
	print("")
	os.system(f"python3 pythonbrute.py -u {user} -ip {ip}{addfile}")
	print("")

def IPScan():
	rede = input("Rede:")
	print("\n--------------------------------")
	os.system("bash ipscan.sh " + rede + "\n")
	print("--------------------------------\n")

def exit():
	sys.exit()

def switcher(argument):
	switch = {
		"1": RunPortScan,
		"2": WebBruteforce,
		"3": DirFinder,
		"4": SSHBruteforce,
		"5": IPScan,
		"6": exit
	}
	return switch.get(argument, "Invalid option")

def main():
	option = ""
	option = input("Choose an option:\n\n"+colored("[+]",color="red")+
		" 1 - PortScanning\n"+colored("[+]",color="red")+
		" 2 - WebBruteforce\n"+colored("[+]",color="red")+
		" 3 - DirFinder\n"+colored("[+]",color="red")+
		" 4 - SSHBruteforce(linux only)\n"+colored("[+]",color="red")+
		" 5 - IP scan(linux only)\n\nOption:")

	if option != "":
		output = switcher(option)
		output()

while True:
	try:
		main()
	except KeyboardInterrupt:
		continue