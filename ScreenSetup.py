# Errita Xu
# May 30, 2023
# FP App - Parent Class
# To setup screen and define variables needed in multiple screens

#import important libraries
from tkinter import *


class ScreenSetup(object):
    
    #attributes maintained the same in all children classes
    user = ''
    month = ''
    datenum = 0
    year = 0
    
    #__init__() - to create screen and attributes all children classes can use (constructor) 
    #@param: self; wn:Window; titleGiven:str
    #@return: none
    def __init__(self, wn, titleGiven):
        
        #create window
        self.win = wn
        #title window based on parameter
        self.win.title(titleGiven)
        #set size + position of the screen
        self.win.geometry('600x900+560+0')
        
        #fonts used throughout the program
        self.titleFont1 = ('Sunflower', 40)
        self.titleFont2 = ('Sunflower', 25)
        self.titleFont3 = ('Sunflower', 60)
        self.bodyFont1 = ('MADE INFINITY PERSONAL USE',24)
        self.bodyFont2 = ('MADE INFINITY PERSONAL USE',20)
        self.bodyFont3 = ('MADE INFINITY PERSONAL USE',15)
        
        #names of accounts and plant folders --> used in multiple children classes to reference the src/dest folders
        self.user_srcFolder_root = './/account_files//'
        self.plant_srcFolder = ".//plant_profiles//"
        
        #define menus
        menu = Menu(self.win)
        self.win.config(menu=menu)
        
        #the navigation menu allows user to go to the previous screen and logout
        self.navMenu = Menu(menu)
        self.navMenu.add_command(label='Previous', command=self.backScreen)
        self.navMenu.add_command(label='Logout', command=self.logout)
        menu.add_cascade(label='Navigation', menu=self.navMenu)
        
        #the command menu allows user to water and journal when in the PlantPreview screen
        self.commandMenu = Menu(menu)
        self.commandMenu.add_command(label='Water')
        self.commandMenu.entryconfig(0, state=DISABLED)
        self.commandMenu.add_command(label='Journal')
        self.commandMenu.entryconfig(1, state=DISABLED)
        menu.add_cascade(label='Commands', menu=self.commandMenu)
        
        #name of all plants added to app
        self.plants = ['Bamboo','Daffodils','Hydrangea','Lithop','Money Tree','Tulips']
        
        #name of each plant's date and journal txt files
        self.plant_files = [['bambooDates.txt', 'bambooJournal.txt'], ['daffodilsDates.txt', 'daffodilsJournal.txt'], ['hydrangeaDates.txt', 'hydrangeaJournal.txt'],
                            ['lithopDates.txt', 'lithopJournal.txt'], ['money_treeDates.txt', 'money_treeJournal.txt'], ['tulipsDates.txt', 'tulipsJournal.txt']]
    
    
    #backScreen() - abstract method to return to previous screen
    #@param: self
    #@return: none
    def backScreen(self):
        pass
    
    
    #logout() - go to Ending screen
    #@param: self
    #@return: none
    def logout(self):
        from Ending import Ending
        self.win.withdraw()
        wn = Ending(Toplevel(self.win), 'Goodbye!')

