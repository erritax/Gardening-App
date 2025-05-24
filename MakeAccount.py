#import important libraries and the parent class
from tkinter import *
from tkinter import messagebox
import os
from ScreenSetup import ScreenSetup


class MakeAccount(ScreenSetup):
    
    #__init__() - to create screen, and make child screen's specific widgets/attributes (constructor) 
    #@param: self
    #@return: none
    def __init__(self, wn, titleGiven):
        
        #run parent class's constructor to initialize screen
        ScreenSetup.__init__(self, wn, titleGiven)
        
        #create frame 1
        #to show welcome quote   
        frameOne = Frame(self.win, bg='honeydew', width=600, height=300)
        frameOne.grid(row=1, columnspan=1)
        frameOne.pack_propagate(False)
        #create label to show welcome quote
        self.welcome_lbl = Label(frameOne, text='Welcome to Sprout 🌱\n\n\nMake Your Account Below', bg='honeydew', font=self.titleFont2)
        self.welcome_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create frame 2
        #to have the user input new a username and password
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=300)
        frameTwo.grid(row=2)
        frameTwo.pack_propagate(False)
        #create label indicating new username
        self.usernameTitle = Label(frameTwo, text='Username:', bg='honeydew', font=self.bodyFont1)
        self.usernameTitle.pack(pady=(40,10))
        #entry box for new username
        self.enter_username = Entry(frameTwo)
        self.enter_username.pack()
        #create label indicating new password
        self.passwordTitle = Label(frameTwo, text='Password:', bg='honeydew', font=self.bodyFont1)
        self.passwordTitle.pack(pady=(40,10))
        #entry box for new password
        self.enter_password = Entry(frameTwo, show='*')     #show * for privacy
        self.enter_password.pack()
        
        #create frame 3
        #to submit new account
        frameThree = Frame(self.win, bg='honeydew', width=600, height=300)
        frameThree.grid(row=3, columnspan=3)
        frameThree.pack_propagate(False)
        #button that triggers account creation
        self.submit_btn = Button(frameThree, text='Submit', font=self.bodyFont1, command=self.test_newAccount)
        self.submit_btn.pack(pady=(50,0))
    
    
    #test_newAccount() - to retrieve user's new username and password, and check validity
    #@param: self
    #@return: none
    def test_newAccount(self):
        
        #retrieve the username and password entered
        username = self.enter_username.get()
        password = self.enter_password.get()
        
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        #set booleans that will validate the new account's username and password
        usernameTaken=False
        usernameWithSpecial=False
        passwordInvalid=False
        
        #check if username is taken
        #open the accountStorage txt file containing all accounts
        f = open(self.user_srcFolder_root+'accountStorage.txt')
        #read txt file
        lines = f.readlines()
        f.close()
        
        accounts= []
        
        #clean reading from txt file (one account per sub-list) - remove \t and \n
        for i in range(0, len(lines)):
            accounts.append(lines[i].split('\t'))
        for i in range(0, len(accounts)):
            for j in range(2):
                if '\n' in accounts[i][j]:
                    check = accounts[i][j]
                    accounts[i][j] = check[0:len(accounts[i][j])-1]
        
        #looping through the app's current accounts, check if the entered username is taken
        for i in range(0, len(accounts)):
            #username is taken
            if username == accounts[i][0]:
                #change boolean value
                usernameTaken = True
                #show messagebox to notify user
                usernameErrorBox = messagebox.showerror(message='Username is taken. Retry!')
                #remove items in entry boxes
                self.enter_username.delete(0, END)
                self.enter_password.delete(0, END)
                break
        
        #username is not taken
        if usernameTaken == False:
            #check if no username was inputted
            if username =='':
                #change boolean value
                usernameWithSpecial=True
                #show messagebox to notify user
                usernameErrorBox = messagebox.showerror(message='Input username before submitting!')
                #remove items in entry boxes
                self.enter_username.delete(0, END)
                self.enter_password.delete(0, END)
            
            #check if username is all leters - no special characters
            for i in range(0, len(username)):
                if username[i].casefold() not in alphabet:
                    #change boolean value
                    usernameWithSpecial = True
                    #show messagebox to notify user
                    usernameErrorBox = messagebox.showerror(message='Username is letters only. Retry!')
                    #remove items in entry boxes
                    self.enter_username.delete(0, END)
                    self.enter_password.delete(0, END)
                    break

            #check if password is valid
            if len(password)<8:
                #change boolean value
                passwordInvalid = True
                #show messagebox to notify user
                passwordErrorBox = messagebox.showerror(message='Your password is too short!\nMin. 8 characters.')
                #remove items in entry boxes
                self.enter_username.delete(0, END)
                self.enter_password.delete(0, END)
        
        #both username and password is valid --> make account
        if usernameTaken==False and usernameWithSpecial==False and passwordInvalid==False:
            self.makeAccount(username, password)
    
    
    #makeAccount() - to make new account (update accountStorage.txt, create new folder + files) based on new username and password
    #@param: self, username:str, password:str
    #@return: none
    def makeAccount(self, username, password): 
                
        #add new account to accountStorage.txt
        f = open(self.user_srcFolder_root + 'accountStorage.txt','a')
        f.write('{}\t{}\tn/a\n'.format(username, password))
        f.close()
                       
        #make new user a new folder
        os.makedirs(self.user_srcFolder_root+username+'//')
        
        #make plant files in the user's new folder
        #self.plant_files is defined in ScreenSetup (parent class) - contain names of all plant txt files
        folder = self.user_srcFolder_root+username+'//'
        for i in range(0, len(self.plant_files)):
            for j in range(2):
                #create file
                f = open(folder+self.plant_files[i][j],'w')
                #if date file, populate with 0s
                if j%2==0:
                    for k in range(6):
                        f.write('0'+'\n')
                f.close()
        
        #display messagebox notifying user of new account
        showDateErrorBox = messagebox.showerror(message='Account Successfully Made!')
        
        #go to Home screen
        self.backScreen()
    
    
    #backScreen() - to take the user to the Home screen
    #@param: self
    #@return: none
    def backScreen(self):
        from Home import Home
        self.win.withdraw()
        wn = Home(Toplevel(self.win), 'Welcome to Sprout!')

