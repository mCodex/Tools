#Simple mouse clicker in Python. Important: You need to install python-xlib to use this script. To do so: pip install python-xlib
#Important this script only works in Unix Systems

import os
from Xlib import X
import Xlib.display as display
from Xlib.ext.xtest import fake_input
import time

def mousepos(screenroot=display.Display().screen().root):
    pointer = screenroot.query_pointer()
    data = pointer._data
    return data["root_x"], data["root_y"]

keyPressed = "true" 

if __name__ == "__main__":

	#data = display.Display().screen().root.query_pointer()._data #used to initilize Xlib
	#print (data["root_x"], data["root_y"]) #If you want uncomment this line and use to get cursor position
	d = display.Display()
	s = d.screen()
	root = s.root

	while (keyPressed == "true"):
		d.sync()
		root.warp_pointer(999,189) #Moving cursor to position 999,189 of the screen
		d.sync()
		fake_input(d, X.ButtonPress, 1) #Mouse Click Event
		d.sync()
		fake_input(d, X.ButtonRelease, 1) #Mouse Click Event
		d.sync()