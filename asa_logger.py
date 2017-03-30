#!/usr/bin/env python3.5

import getpass
import netmiko
import os
import time
import sys

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Print banner
print ("#" * 70)
print ("[*] ASA LOGGING UTILITY")
print ("#" * 70)

# Prompt for ASA IP, username & password
asa_ip = input("Enter ASA IP address: ")
asa_username = input("Enter ASA username: ")
asa_password = getpass.getpass("Enter ASA password: ")
asa_enable_password = getpass.getpass("Enter ASA enable password: ")

# Prompt for IP to focus on
asa_host_focus = input("Enter the host IP address to search for in the logs: ")

# Connect to ASA
try:
	asa_ssh_connection = netmiko.ConnectHandler (
		device_type='cisco_asa',
		ip=asa_ip,
		username=asa_username,
		password=asa_password,
		secret=asa_enable_password
	)
except netmiko.ssh_exception.NetMikoAuthenticationException:
	# Handle authentication failures
	sys.exit("[*] Error: Unable to authenticate")
except netmiko.ssh_exception.NetMikoTimeoutException:
	# Handle timeout failures
	sys.exit("[*] Connection Timeout!")

# Enter enable mode
asa_ssh_connection.enable()

asa_logs = asa_ssh_connection.send_command('show logging asdm')

# Check if asa_host_focus is empty
if asa_host_focus == "":
	asa_show_command = "show logging asdm"
else:
	asa_show_command = "show logging asdm | inc " + asa_host_focus

# Collect logs until Ctrl+C
try:
	while True:
		#Get current logs and append them to the existing variable
		asa_logs += asa_ssh_connection.send_command(asa_show_command)

		#Clear the screen
		os.system('cls' if os.name == 'nt' else 'clear')

		#Print the logs
		print (asa_logs)
		print ("#" * 70)
		print ("[*] Press Ctrl+C to stop")

		#Wait before repeating
		time.sleep(5)
except KeyboardInterrupt:
	pass

# Disconnect SSH session
asa_ssh_connection.disconnect()

# Ask if user would like to save log output to a file
save_file = input("\nWould you like to save the logs to a file [y/n]?: ")

# Check if the user choose to save the logs
if save_file == "y" or save_file == "Y" or save_file == "yes" or save_file == "Yes":
	print ("[*] Saving file asa_logs.txt")

	# Build log file name
	asa_log_file_name = "asa_logs.host.txt"

	# Open the file for writing
	asa_log_file = open ("asa_logs.txt","w")

	# Write variable contents to file
	asa_log_file.write(asa_logs)

	# Close file
	asa_log_file.close()
else:
	sys.exit("[*] Exiting")