# Rick Wallert
# Bonnie Jumpscare
# Cyber Defense Techniques

# SPEC: This is another nuisance tool, meant to be a jumpscare popup of bonnie when run

# Import the GUI stuff
from tkinter import *

# Import OS and random for screen size stuff
import os
import random

# EXE Packaging import
import sys

# Set the master frame to root (we're only using one frame)
root = Tk()

# EXE Packing Information
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Filename for use momentarily, needs to be done this way due to exe packaging
filename = resource_path("bonnie.gif")

# With tkinter, you can't explicitly use gifs.  So, you have to specify each frame within the gif
# Count the number of frames in the gif and pull them apart
frameCount = 5
frames = [PhotoImage(file=filename,format = 'gif -index %i' %(i)) for i in range(frameCount)]

# Method to pull out the individual gif frames
def update(index):
    frame = frames[index]
    index += 1
    if index == frameCount:
        index = 0
    label.configure(image=frame)
    root.after(100, update, index)

# Add the gif into the frame (packed into a label), full screen size
# Pull out screen size
screenDim = os.popen("xdpyinfo | awk \'/dimensions/{print $2}\'").read()
screenLen = int(screenDim.split('x')[0])
screenWid = int(screenDim.split('x')[1])
label = Label(root, width=screenWid, height=screenLen)
label.pack()

# Title the frame
root.title("Do not question the face")

# Run the update method on the root frame starting at frame 0
root.after(0, update, 0)

# Make the frame fullscreen
root.attributes("-fullscreen", True)

# Start the frame
root.mainloop()