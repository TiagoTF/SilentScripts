import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-url', '--url')
parser.add_argument('-w', '--w')
args = parser.parse_args()

fileArgument = args.w

if not fileArgument:
	fileArgument = "rockyou.txt"

file = open(fileArgument, "r")

url = args.url

for i in file:
	try:
		r = requests.get(url+"/"+i.strip())
		if ("200" or "403") in str(r):
			print(url+"/"+i + " Status code: " + str(r))
	except KeyboardInterrupt:
		sys.exit()