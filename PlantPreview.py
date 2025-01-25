# Errita Xu
# May 30, 2023
# FP App - Child Class
# PlantPreview Screen: Personalized plant preview screen; shows facts; allows user to update water date or go to journal

#import important libraries and the parent class
from tkinter import *
from tkinter import messagebox
from ScreenSetup import ScreenSetup


class PlantPreview(ScreenSetup):
    
    #__initi__() - to create screen, and make child screen's specific widgets/attributes (constructor) 
    #@param: self
    #@return: none
    def __init__(self, wn, titleGiven, chosenPlant):
        
        #run parent class's constructor to initialize screen
        ScreenSetup.__init__(self, wn, titleGiven)
        
        self.plantNum=chosenPlant
        
        #configure menu commands with the class's methods
        self.commandMenu.entryconfig(0, command=self.waterPlant)
        self.commandMenu.entryconfig(0, state=NORMAL)         #enable clickability
        self.commandMenu.entryconfig(1, command=self.gotoJournal)
        self.commandMenu.entryconfig(1, state=NORMAL)         #enable clickability
        
        #make photos by sourcing each plant's photo in the plant_srcFolder + converting to PhotoImage
        f = self.plant_srcFolder + 'bamboo_photo.gif'
        self.bamboo_photo = PhotoImage(file = f)
        f = self.plant_srcFolder + 'daffodils_photo.gif'
        self.daffodils_photo = PhotoImage(file = f)
        f = self.plant_srcFolder + 'hydrangea_photo.gif'
        self.hydrangea_photo = PhotoImage(file = f)
        f = self.plant_srcFolder + 'lithop_photo.gif'
        self.lithop_photo = PhotoImage(file = f)
        f = self.plant_srcFolder + 'money_tree_photo.gif'
        self.money_tree_photo = PhotoImage(file = f)
        f = self.plant_srcFolder + 'tulips_photo.gif'
        self.tulips_photo = PhotoImage(file = f)
        
        #add each plant's photos and profile txt file to 2D list
        self.plantprofiles = [['Bamboo', self.bamboo_photo, 'bamboo_profile.txt'], ['Daffodils', self.daffodils_photo, 'daffodils_profile.txt'], 
            ['Hydrangea', self.hydrangea_photo, 'hydrangea_profile.txt'], ['Lithop', self.lithop_photo, 'lithop_profile.txt'], 
            ['Money Tree', self.money_tree_photo, 'money_tree_profile.txt'], ['Tulips', self.tulips_photo, 'tulips_profile.txt']]
        
        #create frame 1
        #to display plant's name
        frameOne = Frame(self.win, bg='honeydew', width=600, height=150)
        frameOne.grid(row=1, columnspan=2)
        frameOne.pack_propagate(False)
        #create label to display the previewing plant's name
        self.plantName = Label(frameOne, bg='honeydew', text=self.plantprofiles[self.plantNum][0], font=self.titleFont1)
        self.plantName.pack(pady=(60,0))
        
        #create frame 2
        #to display the plant's image
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=300)
        frameTwo.grid(row=2, columnspan=2)
        frameTwo.pack_propagate(False)
        #create label containing the plant's image
        self.plantImage = Label(frameTwo, image = self.plantprofiles[self.plantNum][1])
        self.plantImage.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create frame 3
        #to show facts about the plant
        frameThree = Frame(self.win, bg='honeydew', width=600, height=225)
        frameThree.grid(row=3, columnspan=2)
        frameThree.pack_propagate(False)
        #create label containing the facts
        self.plantFacts = Label(frameThree)
        self.plantFacts.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #open file containing the plant's profile (aka facts) + read the txt file
        f = open(self.plant_srcFolder+self.plantprofiles[self.plantNum][2])
        raw_lines = f.readlines()
        f.close()
        #clean the raw data --> ensure correct formatting
        self.lines = ''
        for i in range(0, len(raw_lines)):
            self.lines += raw_lines[i]
        
        #configure the plantFacts label with the plant's profile
        self.plantFacts.config(text=self.lines, bg='honeydew', font=self.bodyFont3)
        
        #create frame 4
        #to display watering command
        frameFour = Frame(self.win, bg='honeydew', width=300, height=225)
        frameFour.grid(row=4, column=0)
        frameFour.pack_propagate(False)
        
        #create frame 5
        #to display journalling command
        frameFive = Frame(self.win, bg='honeydew', width=300, height=225)
        frameFive.grid(row=4, column=1)
        frameFive.pack_propagate(False)
        
        #create attribute storing the name of the user's respective folder
        self.user_folder = self.user_srcFolder_root+self.user+'//'
        #create attribute storing the name of the txt file in question (plant's dates txt file)
        self.file_name = self.plant_files[self.plantNum][0]
        
        #open the file based on folder and file name
        f = open(self.user_folder + self.file_name)
        #read the txt file
        raw_lines = f.readlines()
        f.close()
        
        self.lines = []
        #clean the raw data --> split dates
        for i in range(0, len(raw_lines)):
            self.lines.append(raw_lines[i])
        
        #the last watered date is the first of the txt file
        lastWater_date = self.lines[0]
        if lastWater_date[0]== '0':
            lastWater_date = 'n/a\n'
            
        #the last journalled date is the second of the txt file
        lastJournal_date = self.lines[1]
        if lastJournal_date[0] == '0':
            lastJournal_date = 'n/a\n'
        
        #create label displaying last watered date
        self.lastWatered_lbl = Label(frameFour, bg='honeydew', text='last watered:\n{}'.format(lastWater_date), font=self.bodyFont3)
        self.lastWatered_lbl.pack()
        #create button that triggers change in last watered date
        self.waterBtn = Button(frameFour, text='💧', font=self.titleFont3, command=self.waterPlant)
        self.waterBtn.pack(pady=10)
        
        #create label displaying last journalled date
        self.lastJournaled_lbl = Label(frameFive, bg='honeydew', text='last journaled:\n{}'.format(lastJournal_date), font=self.bodyFont3)
        self.lastJournaled_lbl.pack()
        #create button that triggers the plant's journalling screen
        self.journalBtn = Button(frameFive, text='📕', font=self.titleFont3, command=self.gotoJournal)
        self.journalBtn.pack(pady=10)
    
    
    #waterPlant() - to confirm watering status and update txt file
    #@param: self
    #@return: none
    def waterPlant(self):
        
        #confirm that the user watered the plant
        confirmWaterStatus = messagebox.askquestion(message='Did you water?')
        
        #confirmed that the plant was watered
        if confirmWaterStatus == 'yes':
            #change the last watered date in the list of dates
            self.lines[0] = '{} {}, {}\n'.format(self.month, self.datenum, self.year)
            #open original files and re-write
            f = open(self.user_folder + self.file_name,'w')
            f.writelines(self.lines)
            f.close()
            #configure label with new last watered date
            self.lastWatered_lbl.config(text= 'last watered:\n{} {}, {}\n'.format(self.month, self.datenum, self.year))


    #gotoJournal() - to go to PlantJournal screen
    #@param: self
    #@return: none
    def gotoJournal(self):
        
        #change the last journalled date in the list of dates
        self.lines[1] = '{} {}, {}\n'.format(self.month, self.datenum, self.year)
        
        #open original txt file and re-write
        f = open(self.user_folder + self.file_name,'w')
        f.writelines(self.lines)
        f.close()
        
        #list of possible screen titles based on plant type
        plantJournal_titles = ['Your Bamboo Journal', 'Your Daffodils Journal', 'Your Hydrangea Journal',
                               'Your Lithop Journal', 'Your Money Tree Journal', 'Your Tulips Journal']
        
        #go to the plant's journal screen
        from PlantJournal import PlantJournal
        self.win.withdraw()
        wn = PlantJournal(Toplevel(self.win), plantJournal_titles[self.plantNum], self.plantNum)
    
    
    #backScreen() - go back to the Gallery screen where the user can select a new plant
    #@param: self
    #@return: none
    def backScreen(self):
        from Gallery import Gallery
        self.win.withdraw()
        wn = Gallery(Toplevel(self.win), 'Your Plant Gallery')
        
