# Errita Xu
# May 30, 2023
# FP App - Child Class
# PlantJournal Screen: User can update gardening actions and jot down daily notes

#import important libraries and the parent class
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ScreenSetup import ScreenSetup


class PlantJournal(ScreenSetup):

    #__init__() - to create screen, and make child screen's specific widgets/attributes (constructor) 
    #@param: self
    #@return: none
    def __init__(self, wn, titleGiven, chosenPlant):
        
        #run parent class's constructor to initialize screen
        ScreenSetup.__init__(self, wn, titleGiven)
        
        self.plantNum = chosenPlant
        
        #create frame 1
        #to show plant's name
        frameOne = Frame(self.win, bg='honeydew', width=600, height=150)
        frameOne.grid(row=1, columnspan=1)
        frameOne.pack_propagate(False)
        #create a label with the plant's name
        self.plantName = Label(frameOne, text=self.plants[self.plantNum], bg='honeydew', font=self.titleFont1)
        self.plantName.pack(pady=(60,0))
        
        #create frame 2
        #use checkbutton to track different gardening actions 
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=150)
        frameTwo.grid(row=2)
        frameTwo.pack_propagate(False)
        
        #create IntVar() to hold integer data per possible action
        self.fertilizerChosen = IntVar()
        self.bugCheckChosen = IntVar()
        self.pruneChosen = IntVar()
        self.repotChosen = IntVar()
        
        #create attribute storing the name of the user's personal folder
        self.user_folder = self.user_srcFolder_root+self.user+'//'
        #create attribute storing the plant's dates txt file
        self.file_name = self.plant_files[self.plantNum][0]
        
        #open the file based on folder and file name
        f = open(self.user_folder + self.file_name)
        #read the txt file
        raw_lines = f.readlines()
        f.close()
        lines = []
        
        #clean the raw data --> remove \n
        for i in range(0, len(raw_lines)):
            if raw_lines[i][0] == '0':
                date = 'n/a'
            else:
                date = raw_lines[i]
                date = date[0:len(raw_lines[i])-1]
            lines.append(date)
        
        #create checkbutton for each action
        #per action, add last performed date based on lines ^
        self.fertilizerCheck = Checkbutton(frameTwo, text="Fertilizer (last updated: {})".format(lines[2]), variable=self.fertilizerChosen,bg="honeydew", font=self.bodyFont3)
        self.fertilizerCheck.pack(pady=5)
        self.bugCheckCheck = Checkbutton(frameTwo, text="Bug Check (last updated: {})".format(lines[3]),variable=self.bugCheckChosen,bg="honeydew", font=self.bodyFont3)
        self.bugCheckCheck.pack(pady=5)
        self.pruneCheck = Checkbutton(frameTwo, text="Prune and Pinch (last updated: {})".format(lines[4]),variable=self.pruneChosen,bg="honeydew", font=self.bodyFont3)
        self.pruneCheck.pack(pady=5)
        self.repotCheck = Checkbutton(frameTwo, text="Repot (last updated: {})".format(lines[5]),variable=self.repotChosen,bg="honeydew", font=self.bodyFont3)
        self.repotCheck.pack(pady=5)
        
        #create frame 3
        #to contain the scrollable journal
        frameThree = Frame(self.win, bg='honeydew', width=600, height=450)
        frameThree.grid(row=3)
        frameThree.pack_propagate(False)
        #create scrollable entry box
        self.journal_entry = scrolledtext.ScrolledText(frameThree, wrap = WORD, width = 71, height=32)
        self.journal_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create attribute storing the plant's journal txt file
        self.file_name = self.plant_files[self.plantNum][1]
        #open + read txt file
        f = open(self.user_folder + self.file_name)
        original_entries = f.readlines()
        f.close()
        #insert PREVIOUS entries one line at a time (ensure correct formatting)
        for i in range(0, len(original_entries)):
            self.journal_entry.insert(END, original_entries[i])
        
        #create frame 4
        frameFour = Frame(self.win, bg='honeydew', width=600, height=150)
        frameFour.grid(row=4)
        frameFour.pack_propagate(False)
        #button that triggers journal submission
        self.submitAll = Button(frameFour, text='Submit', bg='honeydew', command=self.submitActions_Journal)
        self.submitAll.pack(pady=50)


    #submitActions_Journal() - to check which actions were selected, update dates, and update journal
    #@param: self
    #@return: none
    def submitActions_Journal(self):
        
        #tracking which actions were performed
        completed_actions = []

        #check which checkbuttons were selected
        if self.fertilizerChosen.get() == 1:
            completed_actions.append("Fertilized")
        if self.bugCheckChosen.get() == 1:
            completed_actions.append("Bug Checked")
        if self.pruneChosen.get() == 1:
            completed_actions.append("Pruned and Pinched")
        if self.repotChosen.get() == 1:
            completed_actions.append("Repotted")
        
        #create attribute storing the name of the user's respective folder
        self.user_folder = self.user_srcFolder_root+self.user+'//'
        #create attribute storing the plant's dates txt file
        self.file_name = self.plant_files[self.plantNum][0]
        
        #open + read txt file        
        f = open(self.user_folder + self.file_name)
        raw_lines = f.readlines()
        f.close()
        
        dates_list = []
        
        #clean txt data --> properly split dates
        for i in range(0, len(raw_lines)):
            dates_list.append(raw_lines[i])
        
        #update date in dates_list IF action was performed 
        if "Fertilized" in completed_actions:
            dates_list[2]='{} {}, {}\n'.format(self.month, self.datenum, self.year)
        if "Bug Checked" in completed_actions:
            dates_list[3]='{} {}, {}\n'.format(self.month, self.datenum, self.year)
        if "Pruned and Pinched" in completed_actions:
            dates_list[4]='{} {}, {}\n'.format(self.month, self.datenum, self.year)
        if "Repotted" in completed_actions:
            dates_list[5]='{} {}, {}\n'.format(self.month, self.datenum, self.year)
        
        #re-write date values in the plant's dates txt file
        f = open(self.user_folder + self.file_name, 'w')
        f.writelines(dates_list)
        f.close()
        
        #get items in the scrollable entry box
        journal = self.journal_entry.get("1.0", tk.END)
        
        #create attribute storing the name of the plant's journal txt file
        self.file_name = self.plant_files[self.plantNum][1]
        
        #open file and re-write with new journal entries
        f = open(self.user_folder + self.file_name, 'w')
        f.write(journal)
        f.close()
        
        #go back to Gallery screen
        self.gotoGallery()


    #gotoGallery() - go back to the Gallery screen where the user can select a new plant 
    #@param: self
    #@return: none
    def gotoGallery(self):
        from Gallery import Gallery
        self.win.withdraw()
        wn=Gallery(Toplevel(self.win), 'Your Plant Gallery')
    
    
    #backScreen() - go back to the PlantPreview screen where the user can water or re-select journalling
    #@param: self
    #@return: none
    def backScreen(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        
        #list of possible screen titles based on plant type
        plantPreview_titles = ['Your Bamboo Preview', 'Your Daffodils Preview', 'Your Hydrangea Preview',
                               'Your Lithop Preview', 'Your Money Tree Preview', 'Your Tulips Preview']
        wn = PlantPreview(Toplevel(self.win), plantPreview_titles[self.plantNum], self.plantNum)
    
