Summary
===
* This script logs into an ASA, grabs the ASDM logs, stores them in a variable and prints the contents of that variable. The grabbing the logs and printing them occurs every five seconds until the script is terminated.
* Version: 1.2

Dependencies
====
* Tested with Python 3.5 & Netmiko 1.2.8
* See requirements.txt for a full list

Setup & Run
====
* Run ASA logger using 'python asa_logger.py' or './asa_logger.py'
* The shebang statement may need to be updated
* Terminating the script can be accomplished using Ctrl+c or cmd+c
* After terminating, the user has the ability to save logs to a file
* The log file will be placed in the same directory from which the script was run