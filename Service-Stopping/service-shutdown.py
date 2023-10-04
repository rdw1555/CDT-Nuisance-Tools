#!/usr/bin/env python3

# Rick Wallert
# Cyber Defense Techniques, Fall 2023
# Team Bravo
# Service-Shutdown

# SPEC: This is a practical tool meant to shut down important services periodically

# Import for OS commands
import os

# Use for service management
import subprocess

# Use time for looping
import time

servicelist = ["apache2", "mysql"]

# Service checking function, check if any services are active and stop them if they are
def service_check():
    # Loop over every process in the servicelist
    for service in servicelist:
        # Check if it's active or not (output wil be either "active" or "inactive")
        p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')

        if "in" not in output:
            # Stop the service and disable it
            stopcom = "sudo systemctl stop " + service
            disablecom = "sudo systemctl disable " + service
            os.popen(stopcom)
            os.popen(disablecom)

# Loop forever
while(True):
    # Run a check every 15 seconds
    time.sleep(15)
    service_check()