#This script is to do a basic ping, to do two things, test internet conectivity 
# and ensuring all troubleshooting steps are taken

import os

# Defining common variables with their name
# This is so the list can be as dynamic as possible
Printer = "EPSONFC30C3"
Repeater = "RE200"
Modem = "Telstra"
LOOPBACK = "Loopback"
internet = "google.com"


# Creating a list will all devices to test connectivity with
ip_list = [LOOPBACK, Modem, Repeater, Printer, internet]

# Using a loop to go through the list and pinrt out the results 
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" and "Approximate" in response:
        print(f"UP: {ip} Ping Successful")
    elif "Received = 0" and "Approximate" in response:
        print(f"DOWN: {ip} Ping Failed")
    else:
        print(f"{ip} {response}")
