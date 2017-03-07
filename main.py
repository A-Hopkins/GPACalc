"""
GPACalc
Alex
3/4/2017

The goal of this project is to create a GPA calculator, that can take in future classes, past classes, and current
classes. And displaying the information in a GUI. This is the main file which consists of the mainloop
"""

from tkinter import Tk
from gui import GUI

# Start of the Tk() method
root = Tk()

# Start the GUI
app = GUI(root)

# Mainloop
root.mainloop()
