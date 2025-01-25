# Errita Xu
# May 30, 2023
# FP App - Child Class
# Home Screen: User logins or has the option to make an account

#import important libraries and the parent class
from tkinter import *
from tkinter import messagebox
from ScreenSetup import ScreenSetup


class Home(ScreenSetup):
    
    #__init__() - to create screen, and make child screen's specific widgets/attributes (constructor) 
    #@param: self, wn:Window; titleGiven:str
    #@return: none
    def __init__(self, wn, titleGiven):
        ScreenSetup.__init__(self, wn, titleGiven)
        
        #disable logging out command in menu
        self.navMenu.entryconfig(1, state=DISABLED)
        
        #create frame 1
        #to welcome user
        frameOne = Frame(self.win, bg='honeydew', width=600, height=300)
        frameOne.grid(row=1, columnspan=1)
        frameOne.pack_propagate(False)              #pack propogate --> frame won't resize after widgets are added
        #create label with title
        self.titleLabel = Label(frameOne, text='Welcome to \nSprout 🌱 !', bg = 'honeydew', font=self.titleFont1)
        self.titleLabel.place(relx=0.5, rely=0.6, anchor=CENTER)             #centers the label
        
        #create frame 2
        #to enable user to enter username and password
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=300)
        frameTwo.grid(row=2, columnspan=1)
        frameTwo.pack_propagate(False)
        #create username title - label
        self.usernameTitle = Label(frameTwo, text='Username:', bg='honeydew', font=self.bodyFont1)
        self.usernameTitle.grid(row=1, padx=235, pady=(30,15))
        #create username entry box
        self.usernameEnter = Entry(frameTwo, width=35)
        self.usernameEnter.grid(row=2)
        #create password title - label
        self.passwordTitle = Label(frameTwo, text='Password:', bg='honeydew', font=self.bodyFont1)
        self.passwordTitle.grid(row=3, padx=235, pady=(30,15))
        #create password entry box
        self.passwordEnter = Entry(frameTwo, width=35, show='*')        #show * to ensure privacy
        self.passwordEnter.grid(row=4)
        #button to trigger username and password submission
        self.loginBtn = Button(frameTwo,text="Login",command=self.submit_login, font=self.bodyFont1)
        self.loginBtn.grid(row=5, pady=(35,50))
        
        #create frame 3
        #allow user to create a Sprout account
        frameThree = Frame(self.win, bg='honeydew', width=600, height=300)
        frameThree.grid(row=3, columnspan=1)
        frameThree.pack_propagate(False)
        #create label to ask if the user has an account
        self.noAccountTitle = Label(frameThree, text='No Account?', bg='honeydew', font=self.bodyFont1)
        self.noAccountTitle.grid(row=1, padx=220, pady=30)
        #button to trigger account creation --> go to MakeAccount screen
        self.createAccountBtn = Button(frameThree, text='Create Account', bg='honeydew', command=self.create_account, font=self.bodyFont1)
        self.createAccountBtn.grid(row=2, pady=(0,155))
        
    #submit_login() - to retrieve login values entered and validate
    #@param: self
    #@return: none
    def submit_login(self):
        
        #retrieve the username and password entered
        username = self.usernameEnter.get()
        password = self.passwordEnter.get()
        
        #open accountStorage txt file that stores all account login info and read the file
        f = open(self.user_srcFolder_root+'accountStorage.txt')
        lines = f.readlines()
        accounts= []
        #split and clean data to create 2D list (1 sublist per account)
        for i in range(0, len(lines)):
            accounts.append(lines[i].split('\t'))
        for i in range(0, len(accounts)):
            for j in range(2):
                if '\n' in accounts[i][j]:
                    check = accounts[i][j]
                    accounts[i][j] = check[0:len(accounts[i][j])-1]
        f.close()
                
        user_found = False      #this variable will change when username is found in accountStorage
        
        #using a for loop, loop through each account to see if username exists
        for i in range(0, len(accounts)):
            #when the username is found
            if username == accounts[i][0]:
                user_found = True           #change boolean value
                
                #when the password corresponds to the username
                if password == accounts[i][1]:
                    #update user attribute value (located in parent class)
                    ScreenSetup.user = username
                    
                    #go to Date_Feelings screen
                    from Date_Feelings import Date_Feelings
                    self.win.withdraw()
                    wn = Date_Feelings(Toplevel(self.win), 'Hi there!')
                    
                #username correct but password incorrect
                else:
                    #clear values in the password entry box
                    self.passwordEnter.delete(0, END)
                    #notify user of incorrect password
                    showLoginError = messagebox.showerror(message='Incorrect Password!')
                    break
        
        #entered username not found        
        if user_found == False:
            
            #clear values in the username and password entry boxes
            self.usernameEnter.delete(0, END)
            self.passwordEnter.delete(0, END)
            
            #notify user of unsuccessful login
            showLoginError = messagebox.showerror(message='Account Not Found!')
    
    
    #create_account() - go to the MakeAccount screen where the user can make a new account
    #@param: self
    #@return: none
    def create_account(self):
        from MakeAccount import MakeAccount
        self.win.withdraw()
        wn = MakeAccount(Toplevel(self.win), 'Make Your Sprout Account!')
    
    
    #backScreen() - notifies the user that there is no prior screen and they must login
    #@param: self
    #@return: none
    def backScreen(self):
        showMessageBox = messagebox.showerror(message='You must login first!')

