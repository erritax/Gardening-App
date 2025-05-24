#import important libraries and the parent class
from tkinter import *
from tkinter import messagebox
from ScreenSetup import ScreenSetup


class Date_Feelings(ScreenSetup):
    
    #__init__() - to create screen, and make child screen's specific widgets/attributes (constructor) 
    #@param: self, wn:Window; titleGive:str
    #@return: none
    def __init__(self, wn, titleGiven):
        
        #run parent class's constructor to initialize screen
        ScreenSetup.__init__(self, wn, titleGiven)
        
        #create frame 1
        #to display opening quote
        frameOne = Frame(self.win, bg='honeydew', width=600, height=300)
        frameOne.grid(row=1, columnspan=1)
        frameOne.pack_propagate(False)
        #create label for opening quote
        self.quoteLabel = Label(frameOne, text='Keep Going,\nKeep Growing!', bg = 'honeydew', font=self.titleFont1)
        self.quoteLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create frame 2
        #to show "Today's Date" title
        frameTwo = Frame(self.win, bg='honeydew', width=600, height=50)
        frameTwo.grid(row=2)
        frameTwo.pack_propagate(False)
        #create label for title
        self.dateTitle = Label(frameTwo, text='Today\'s Date:', bg='honeydew', font=self.bodyFont1)
        self.dateTitle.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #create frame 3
        #to collect date values (month, date num, year)
        frameThree = Frame(self.win, bg='honeydew', width=600, height=150)
        frameThree.grid(row=3, columnspan=3)
        frameThree.pack_propagate(False)
        
        #create label to display month title
        self.monthLbl = Label(frameThree, text='Month:', bg='honeydew', font=self.bodyFont3)
        self.monthLbl.grid(row=1, column=1, padx=(100,25), pady=(30, 0))
        #create month entry box
        self.dateMonthEnter = Entry(frameThree, width=10)
        self.dateMonthEnter.grid(row=2, column=1, padx=(100,25), pady=(10,50))
        
        #create label to display date num title
        self.numLbl = Label(frameThree, text='Day:', bg='honeydew', font=self.bodyFont3)
        self.numLbl.grid(row=1, column=2, padx=22.5, pady=(30, 0))
        #create date num entry box
        self.dateDayEnter = Entry(frameThree, width=10)
        self.dateDayEnter.grid(row=2, column=2, padx=22.5, pady=(10,50))
        
        #create label to display year title
        self.yearLbl = Label(frameThree, text='Year:', bg='honeydew', font=self.bodyFont3)
        self.yearLbl.grid(row=1, column=3, padx=(25,100), pady=(30, 0))
        #create year entry box
        self.dateYearEnter = Entry(frameThree, width=10)
        self.dateYearEnter.grid(row=2, column=3, padx=(25,100), pady=(10,50))
        
        #create frame 4
        #to ask user how they are feeling
        frameFour = Frame(self.win, bg='honeydew', width=600, height=100)
        frameFour.grid(row=4, columnspan=3)
        frameFour.pack_propagate(False)
        #create label asking feelings question
        self.feelingsQuestion = Label(frameFour, text='How are you feeling today?', bg='honeydew', font=self.bodyFont1)
        self.feelingsQuestion.pack(pady=15)
        
        #create frame 5
        #to display emotion options       
        frameFive = Frame(self.win, bg='honeydew', width=600, height=100)
        frameFive.grid(row=5, columnspan=3)
        frameFive.pack_propagate(False)
        #create button with happy emoji
        self.goodBtn=Button(frameFive, text='😄', font=self.titleFont3)
        self.goodBtn.grid(row=2, column=1, padx=(110, 20))
        #create button with mid emoji
        self.mediumBtn=Button(frameFive, text='😐', font=self.titleFont3)
        self.mediumBtn.grid(row=2, column=2, padx=25)
        #create button with mad emoji
        self.badBtn=Button(frameFive, text='😡', font=self.titleFont3)
        self.badBtn.grid(row=2, column=3, padx=(20, 110))
        
        #create frame 6
        #to submit date and feelings response
        frameSix = Frame(self.win, bg='honeydew', width=600, height=240)
        frameSix.grid(row=6, columnspan=1)
        frameSix.pack_propagate(False)
        #create button that triggers submission
        self.submitFeelingsAndDate = Button(frameSix, text='Submit', bg='honeydew', command=self.submitDate, font=self.bodyFont1)
        self.submitFeelingsAndDate.pack(pady=(50,0))
    
    
    #submitDate() - to retrieve submitted date values and check if valid
    #@param: self
    #@return: none
    def submitDate(self):
        
        #lists containing each month and max date num
        #note: this app doesn't consider leap years
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        dates_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        #retrieve entered values from entry boxes
        entered_month = self.dateMonthEnter.get()
        entered_num = self.dateDayEnter.get()
        entered_year = self.dateYearEnter.get()
        
        #create list that will track the submission's validity
        errors = []
        
        #not a valid month
        if entered_month.casefold() not in months:
            errors.append('month')
            
            #check if entered date num is an integer
            try:
                entered_num = int(entered_num)
            
            #not an integer
            except ValueError:
                errors.append('number')  
        
        #valid month, so check if the date number is valid
        else:
            for i in range(0, len(months)):
                #'i' represents the month's order in the year
                if entered_month.casefold() == months[i]:
                    
                    #check if enetered date num is an integer
                    try:
                        entered_num = int(entered_num)
                        
                        #date number is over the max number of days in a month or is negative
                        if entered_num>dates_max[i] or entered_num<=0:
                            errors.append('number')
                            
                    #not an integer, invalid
                    except ValueError:
                        errors.append('number')
                    break
                
        #check if entered year is valid (integer not greater than 2023)
        try:
            entered_year = int(entered_year)
            
            #year is in the future or before CE
            if entered_year>2023 or entered_year<0:
                errors.append('year')
                
        #not an integer, invalid
        except ValueError:
            errors.append('year')
        
        
        valid = True
        #check if date is valid (not past date) given no errors in entry
        #check previous login date
        if len(errors) == 0:
            #open accountStorage txt file and read the file
            f = open(self.user_srcFolder_root+'accountStorage.txt')
            raw_lines = f.readlines()
            lines= []
            #clean data to create 2D list (one sublist per account)
            for i in range(0, len(raw_lines)):
                lines.append(raw_lines[i].split('\t'))
            for i in range(0, len(lines)):
                for j in range(0, len(lines[i])):
                    if '\n' in lines[i][j]:
                        check = lines[i][j]
                        lines[i][j] = check[0:len(lines[i][j])-1]
            f.close()
            
            #using a for loop, identify which sublist corresponds to the user
            for i in range(0, len(lines)):
                if self.user == lines[i][0]:
                    #new account (no last login date)
                    if 'n/a' == lines[i][2]:
                        break
                    
                    #retrieve last login date values based on index value (order)
                    else:
                        lastlogin_month = lines[i][2]
                        lastlogin_num = lines[i][3]
                        lastlogin_year = lines[i][4]
                    
                    #check if the entered year is before the last login date's year
                    if int(lastlogin_year)>entered_year:
                        errors.append('past')
                        break
                    
                    #if the same year...
                    elif int(lastlogin_year)==entered_year:
                        
                        #identify the month number of last login's month and the entered month
                        lastlogin_month_index = months.index(lastlogin_month.casefold())
                        entered_month_index = months.index(entered_month.casefold())
                        
                        #entered month is before last login's month
                        if lastlogin_month_index>entered_month_index:
                            errors.append('past')
                            break
                        
                        #same month
                        elif lastlogin_month_index==entered_month_index:
                            
                            #check if date number entered and last login's date num
                            if int(lastlogin_num)>int(entered_num):
                                errors.append('past')
                            else:
                                break
                        else:
                            break
                    else:
                        break
        
        #entered date is invalid due to invalid value or date in the past
        if len(errors)!=0 or valid!=True:
            
            string = 'invalid: '
            
            #notify the user that the entered date is in the past
            if 'past' in errors:
                string += '\ndate is in the past'
            
            #notify the user the specific values that are invalid
            else:
                if len(errors)==1:
                    string += errors[0]
                elif len(errors)==2:
                    string += errors[0] + ' and ' + errors[1]
                elif len(errors)==3:
                    string += errors[0] + ', ' + errors[1] + ', and ' + errors[2]
            
            #clear the entry boxes for those with invalid values
            if 'month' in errors or 'past' in errors:
                self.dateMonthEnter.delete(0, END)
            if 'number' in errors or 'past' in errors:
                self.dateDayEnter.delete(0, END)
            if 'year' in errors or 'past' in errors:
                self.dateYearEnter.delete(0, END)
            
            #notify user of the error(s) using a messagebox
            showDateErrorBox = messagebox.showerror(message=string)
        
        #entered date is valid
        else:
            #update date attribute values (located in the parent class)
            ScreenSetup.month = entered_month.capitalize()
            ScreenSetup.datenum = entered_num
            ScreenSetup.year = entered_year
            
            #update the user's last login date value in accountStorage.txt
            for i in range(0, len(lines)):
                #row i corresponds to the logged in user
                #update row with new date
                if self.user==lines[i][0]:
                    if 'n/a' in lines[i]:
                        lines[i][2]=entered_month.capitalize()
                        lines[i].append(str(entered_num))
                        lines[i].append(str(entered_year))
                    else:
                        lines[i][2]=entered_month.capitalize()
                        lines[i][3]=str(entered_num)
                        lines[i][4]=str(entered_year)
                    break
            
            #write new txt file lines
            f = open(self.user_srcFolder_root+'accountStorage.txt', 'w')
            for i in range(0, len(lines)):
                #write in txt file with correct formatting
                for j in range(4):
                    f.write(lines[i][j]+'\t')
                f.write(lines[i][4]+'\n')
            f.close()
            
            #go to the plant gallery screen
            self.galleryScreen()   
    
    
    #galleryScreen() - go to the Gallery screen where the user can see all documented plants
    #@param: self
    #@return: none
    def galleryScreen(self):
        from Gallery import Gallery
        self.win.withdraw()
        wn = Gallery(Toplevel(self.win), 'Your Plant Gallery')
    
    
    #backScreen() - go to the Home screen where the user can re-login
    #@param: self
    #@return: none
    def backScreen(self):
        from Home import Home
        self.win.withdraw()
        wn = Home(Toplevel(self.win), 'Welcome to Sprout!')

