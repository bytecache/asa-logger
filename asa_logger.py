#!/usr/bin/env python3.5

import getpass
import netmiko
import os
import time

#Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

#print banner
terminal_width = os.get_terminal_size()
print ("=" * terminal_width.columns)
print ("ASA Logging Utility".center(terminal_width.columns))
print ("-" * terminal_width.columns)
print ("Description: Connects to an ASA and collects the contents on the logs")
print ("Author: Codename")
print ("=" * terminal_width.columns)

#prompt for ASA IP, username & password
asa_ip = input("Enter ASA IP address: ")
asa_username = input("Enter ASA username: ")
asa_password = getpass.getpass("Enter ASA password: ")
asa_enable_password = getpass.getpass("Enter ASA enable password: ")

#Prompt for IP to focus on
asa_host_focus = input("Enter the host IP address to search for in the logs: ")

#Connect to ASA
asa_ssh_connection = netmiko.ConnectHandler (
	device_type='cisco_asa',
	ip=asa_ip,
	username=asa_username,
	password=asa_password,
	secret=asa_enable_password
)

#Enter enable mode
asa_ssh_connection.enable()

asa_logs = asa_ssh_connection.send_command('show logging asdm')

#loop
try:
	while True:
		#Get current logs and append them to the existing variable
		asa_logs += asa_ssh_connection.send_command('show logging asdm')

		#Clear the screen
		os.system('cls' if os.name == 'nt' else 'clear')

		#Print the logs
		print (asa_logs)

		#Wait before repeating
		time.sleep(5)
except KeyboardInterrupt():
	pass

#Disconnect SSH session
asa_ssh_connection.disconnect()