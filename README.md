Summary
===
* This script logs into an ASA, grabs the ASDM logs, stores them in a variable and prints the contents of that variable. The grabbing the logs and printing them occurs every five seconds until the script is terminated.
* Version: 1.0

Dependancies
====
* Tested with Python 3.5 & Netmiko 1.2.8

Setup & Run
====
* Run ASA logger using 'python asa_logger.py' or './asa_logger.py'
* The shebang statement may need to be updated