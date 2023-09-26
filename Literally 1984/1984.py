# Rick Wallert
# Literally 1984
# Cyber Defense Techniques

# SPEC: This is another nuisance tool, meant to pop up an animated gif on screen repeatedly

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
filename = resource_path("1984.gif")

# With tkinter, you can't explicitly use gifs.  So, you have to specify each frame within the gif
# Count the number of frames in the gif and pull them apart
frameCount = 30
frames = [PhotoImage(file=filename,format = 'gif -index %i' %(i)) for i in range(frameCount)]

# Method to pull out the individual gif frames
def update(index):
    frame = frames[index]
    index += 1
    if index == frameCount:
        index = 0
    label.configure(image=frame)
    root.after(100, update, index)

# Method to move the window when the close button is clicked
def close_prevention():
    # Silly little message
    print("Not gonna happen")

    # Pull out screen size
    screenDim = os.popen("xdpyinfo | awk \'/dimensions/{print $2}\'").read()
    screenLen = screenDim.split('x')[0]
    screenWid = screenDim.split('x')[1]

    # Choose a random number within 0 to len size and 0 to wid size
    ranLen = random.randint(0, int(screenLen))
    ranWid = random.randint(0, int(screenWid))
    
    # Move the frame to a random position on the screen
    movement = "+" + str(ranLen) + "+" + str(ranWid)
    root.geometry(movement)

# Add the gif into the frame (packed into a label)
label = Label(root)
label.pack()

# Title the frame
root.title("Do not question the face")

# Run the update method on the root frame starting at frame 0
root.after(0, update, 0)

# Add the protocol to prevent the window close
root.protocol("WM_DELETE_WINDOW", close_prevention)

# Start the frame
root.mainloop()