from tkinter import *

#import parent class
from ScreenSetup import ScreenSetup

#import child classes
from Home import Home
from Date_Feelings import Date_Feelings
from Gallery import Gallery
from PlantPreview import PlantPreview
from PlantJournal import PlantJournal
from Ending import Ending
from MakeAccount import MakeAccount

#create window and run the Home child class
window = Tk()
win = Home(window, 'Welcome to Sprout!')
window.mainloop()
