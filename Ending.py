#import important libraries and the parent class
from tkinter import *
from tkinter import messagebox
import random
from ScreenSetup import ScreenSetup


class Ending(ScreenSetup):
    
    #__init__() - to create screen, and make child screen's specific widgets/attributes (constructor) 
    #@param: self
    #@return: none
    def __init__(self, wn, titleGiven):
        
        #run parent class's constructor to initialize screen
        ScreenSetup.__init__(self, wn, titleGiven)
        
        #disable logging out command in menu
        self.navMenu.entryconfig(1, state=DISABLED)
        
        #create frame 1
        #say goodbye!
        frameOne = Frame(self.win, bg='honeydew', width=600, height=550)
        frameOne.grid(row=1, columnspan=1)
        frameOne.pack_propagate(False)
        #create label saying bye
        self.bye_label = Label(frameOne, text='Bye 👋', bg='honeydew', font=self.titleFont3)
        self.bye_label.pack(pady=(100,50))
        #create label with Sprout's logo
        self.bye_logo = Label(frameOne, text='🌱', bg='honeydew', font=('Arial', 180))
        self.bye_logo.pack()
        
        #create frame 2
        #to show a cheesy plant-related quote
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=125)
        frameTwo.grid(row=2)
        frameTwo.pack_propagate(False)
        #list of possible quotes
        self.funnyQuotes = ['What did the husband say when his wife\ntold him he bought the wrong flowers? \n\nOopsie daisy!', 'If I had a trillium dollars...', 
                         'How does a flower whistle?\n\nBy using its tulips.', 'Hey, bud! How’s it growing?', 'How do trees get on Instagram?\n\nThey log in', 
                         'I’m rooting for you!']
        #randomly choose a quote
        self.chosen = random.choice(self.funnyQuotes)
        #create label that displays the chosen funny quote
        self.fun_label = Label(frameTwo, text=self.chosen, bg='honeydew', font=self.bodyFont2)
        self.fun_label.pack()
        
        #create frame 3
        #allow user to re-login --> go back to Home screen
        frameThree = Frame(self.win, bg='honeydew', width=600, height=225)
        frameThree.grid(row=3, columnspan=3)
        frameThree.pack_propagate(False)
        #create button that triggers re-login
        self.reloginBtn = Button(frameThree, text = 'Re-Login', command = self.relogin, font=self.bodyFont1)
        self.reloginBtn.pack(pady=50)
    
    
    #relogin() - to take the user back to the Home screen
    #@param: self
    #@return: none
    def relogin(self):
        from Home import Home
        self.win.withdraw()
        wn = Home(Toplevel(self.win), 'Welcome to Sprout!')
    
    
    #backScreen() - show message that the user has been logged out and must re-login
    #@param: self
    #@return: none
    def backScreen(self):
        mustReLoginMessage = messagebox.showinfo(message='You must re-login!')

