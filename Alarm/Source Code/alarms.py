# Rick Wallert
# Alarms
# Cyber Defense Techniques

# SPEC: This is a nuisance tool to play alarm sounds to freak out the blue team
# Disclaimer: I do not know if there are speakers hooked up to the boxes in the cyber range
# So, there is a chance that this straight up will not do anything

# Audio import
from playsound import playsound

# Random import
import random

# Time import
import time

# OS import
import os

# sys import
import sys

# EXE Packing Information
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Loop infinitely
while(True):
    # Choose a random alarm sound
    randomalarm = random.randint(1,10)
    alarm = "alarm" + str(randomalarm) + ".mp3"

    # Get the filepath (needed for EXE packing)
    filepath = resource_path(alarm)

    # Play the alarm
    playsound(filepath)

    # Wait a random amount of time between 1 and 3 minutes, and then repeat
    waitrand = random.randint(1,3)
    timewait = waitrand * 60
    time.sleep(timewait)