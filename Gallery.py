# Errita Xu
# May 30, 2023
# FP App - Child Class
# Gallery Screen: Displays all the plant options as buttons and takes to preview screen when clicked

#import important libraries and the parent class
from tkinter import *
from ScreenSetup import ScreenSetup


class Gallery(ScreenSetup):
    
    #__init__() - to create screen, and make child screen's specific widgets/attributes (constructor)
    #@param: self; wn:Window; titleGive:str
    #@return: none
    def __init__(self, wn, titleGiven):
        
        #run parent class's constructor to initialize screen
        ScreenSetup.__init__(self, wn, titleGiven)
        
        #create frame 1
        #to display the gallery's title
        frameOne = Frame(self.win, bg='honeydew', width=600, height=175)
        frameOne.grid(row=1, columnspan=2)
        frameOne.pack_propagate(False)
        #create label for title
        self.galleryTitle = Label(frameOne, text='Welcome to Your\nPlant Gallery 🪴!', bg = 'honeydew', font=self.titleFont2)
        self.galleryTitle.pack()
        self.galleryTitle.pack(pady=(50,0))
        
        #photos for buttons --> access file name in src folder and convert to PhotoImage
        f = self.plant_srcFolder + 'bamboo_small.gif'
        self.bamboo_photo_small = PhotoImage(file = f)
        f = self.plant_srcFolder + 'daffodils_small.gif'
        self.daffodils_photo_small = PhotoImage(file = f)
        f = self.plant_srcFolder + 'hydrangea_small.gif'
        self.hydrangea_photo_small = PhotoImage(file = f)
        f = self.plant_srcFolder + 'lithop_small.gif'
        self.lithop_photo_small = PhotoImage(file = f)
        f = self.plant_srcFolder + 'money_tree_small.gif'
        self.money_tree_photo_small = PhotoImage(file = f)
        f = self.plant_srcFolder + 'tulips_small.gif'
        self.tulips_photo_small = PhotoImage(file = f)
        
        #create frame 2
        #to display the 6 plant options as image buttons --> use gridding to properly format
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=500)
        frameTwo.grid(row=2, columnspan=2)
        frameTwo.pack_propagate(False)
        #create title and button (w/ corresponding image) for bamboo
        bamboo_btn = Button(frameTwo, image = self.bamboo_photo_small, command = self.bamboo_click)
        bamboo_btn.grid(row=0, column=0, padx=(10,5))
        bamboo_lbl = Label(frameTwo, text='Bamboo', bg='honeydew', font=self.bodyFont2)
        bamboo_lbl.grid(row=1, column=0, pady=(10, 30))
        #create title and button (w/ corresponding image) for daffodils
        daffodils_btn = Button(frameTwo, image = self.daffodils_photo_small, command = self.daffodils_click)
        daffodils_btn.grid(row=0, column=1, padx=(5,10))
        daffodils_lbl = Label(frameTwo, text='Daffodils', bg='honeydew', font=self.bodyFont2)
        daffodils_lbl.grid(row=1, column=1, pady=(10, 30))
        #create title and button (w/ corresponding image) for hydrangea
        hydrangea_btn = Button(frameTwo, image = self.hydrangea_photo_small, command = self.hydrangea_click)
        hydrangea_btn.grid(row=2, column=0, padx=(10,5))
        hydrangea_lbl = Label(frameTwo, text='Hydrangea', bg='honeydew', font=self.bodyFont2)
        hydrangea_lbl.grid(row=3, column=0, pady=(10, 30))
        #create title and button (w/ corresponding image) for lithop
        lithop_btn = Button(frameTwo, image = self.lithop_photo_small, command = self.lithop_click)
        lithop_btn.grid(row=2, column=1, padx=(5,10))
        lithop_lbl = Label(frameTwo, text='Lithop', bg='honeydew', font=self.bodyFont2)
        lithop_lbl.grid(row=3, column=1, pady=(10, 30))
        #create title and button (w/ corresponding image) for money tree
        money_tree_btn = Button(frameTwo, image = self.money_tree_photo_small, command = self.money_tree_click)
        money_tree_btn.grid(row=4, column=0, padx=(10,5))
        money_tree_lbl = Label(frameTwo, text='Money Tree', bg='honeydew', font=self.bodyFont2)
        money_tree_lbl.grid(row=5, column=0, pady=(10, 35))
        #create title and button (w/ corresponding image) for tulips
        tulips_btn = Button(frameTwo, image = self.tulips_photo_small, command = self.tulips_click)
        tulips_btn.grid(row=4, column=1, padx=(5,10))
        tulips_lbl = Label(frameTwo, text='Tulips', bg='honeydew', font=self.bodyFont2)
        tulips_lbl.grid(row=5, column=1, pady=(10, 35))
    
    
    #bamboo_click() - go to the PlantPreview screen where the user can update actions on the user's Bamboos
    #@param: self
    #@return: none
    def bamboo_click(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        wn = PlantPreview(Toplevel(self.win), 'Your Bamboo Preview', 0)
    
    
    #daffodils_click() - go to the PlantPreview screen where the user can update actions on the user's Daffodils
    #@param: self
    #@return: none
    def daffodils_click(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        wn = PlantPreview(Toplevel(self.win), 'Your Daffodils Preview', 1)
    
    
    #hydrangea_click() - go to the PlantPreview screen where the user can update actions on the user's Hydrangeas
    #@param: self
    #@return: none
    def hydrangea_click(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        wn = PlantPreview(Toplevel(self.win), 'Your Hydrangea Preview', 2)
    
    
    #lithop_click() - go to the PlantPreview screen where the user can update actions on the user's Lithops
    #@param: self
    #@return: none
    def lithop_click(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        wn = PlantPreview(Toplevel(self.win), 'Your Lithop Preview', 3)
    
    
    #money_tree_click() - go to the PlantPreview screen where the user can update actions on the user's Money Tree
    #@param: self
    #@return: none
    def money_tree_click(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        wn = PlantPreview(Toplevel(self.win), 'Your Money Tree Preview', 4)
    
    
    #tulips_click() - go to the PlantPreview screen where the user can update actions on the user's Tulips
    #@param: self
    #@return: none
    def tulips_click(self):
        from PlantPreview import PlantPreview
        self.win.withdraw()
        wn = PlantPreview(Toplevel(self.win), 'Your Tulips Preview', 5)


    #backScreen() - go to the Date_Feelings screen where the user can enter date
    #@param: self
    #@return: none
    def backScreen(self):
        from Date_Feelings import Date_Feelings
        self.win.withdraw()
        wn = Date_Feelings(Toplevel(self.win), 'Hi there!')
    
    