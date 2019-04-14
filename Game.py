#########################################################################################################################################
##                  Importing the required imports for the Gui, and File Reading                                                       ##
#########################################################################################################################################
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
#########################################################################################################################################
##                  Opening the Login_Data file for the Users                                                                          ##
#########################################################################################################################################
with open("login_data.txt", "r") as login_file:
    try:
        users = json.load(login_file)
    except:
        users = {}
        

#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                     STARTING THE MAIN GUI WITH THE ROOT.MAINLOOP()                                                  ##
##                                     AND STARTING THE LOG IN CLASS AS ITS FIRST GUI                                                  ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
######################################################################################################################################### 
class Login:
#########################################################################################################################################
##                        Initializing the Login Window                                                                                ##
#########################################################################################################################################
    def __init__(self, master):
        #This sets the self.master
        self.master = master
        #This sets the Title, Background Colour and icon
        master.configure(background = "#959595")
        self.master.title("Login")
        self.master.iconbitmap("login.ico")
        #This sets the Labels, Buttons and Entries
        self.lblname = Label(master, text="Name", fg="black", bg="#959595", font=("Helvetica", 12, "underline"))
        self.lblname.grid(row=0)
        self.lblpass = Label(master, text="Pass", fg="black", bg="#959595", font=("Helvetica", 12, "underline"))
        self.lblpass.grid(row=1)
        self.btnlogin = Button(master, text="Login", command=self.Login, font=("Helvetica", 10, "bold"), relief='flat', bg="#F0A757")
        self.btnlogin.grid(row=3, column=1)
        self.btnreg = Button(master, text="Register", command=self.Registerwindow, font=("Helvetica", 10, "bold"), relief='flat', bg="#D94A68")
        self.btnreg.grid(row=3, column=3)
        self.btnforg = Button(master, text="Forgot Pass", command=self.Forgotwindow, font=("Helvetica", 10, "bold"), relief='flat', bg="#4B62E0")
        self.btnforg.grid(row=3, column=0)
        self.entname = Entry(master)
        self.entname.grid(row=0, column=1)
        self.entpass = Entry(master, show="*")
        self.entpass.grid(row=1, column=1)

#########################################################################################################################################
##                     The Login Button                                                                                                ##
#########################################################################################################################################
    def Login(self):
        """This Calls for the name and password
From the 2 entrys and checks if they are in the
Login_data.txt file, and if they are then its a user
and will set up a global call crntLogin to the user name
so other classes can easily access the users login name
that was used in the entry.
After all of this is done, it will load the window
to choose if you want to Start a new game or Load
a new one, then it will destroy all of the slaves
on the main window, ready for the window to become
the host for the Maze_Game
If the Users name does not match up it will display an error
message."""
        global users
        global crntLogin
        username = self.entname.get()
        password = self.entpass.get()
        if username in users and users[username] == password:
            crntLogin = username
            self.newWindow = Toplevel(self.master)
            self.app = LoadorSave(self.newWindow)
            self.clear()
        else:
            messagebox.showerror("Failed", "Username or Password is incorrect")
#########################################################################################################################################
##                       The Register and Forgot Password Buttons                                                                      ##
#########################################################################################################################################
    def Registerwindow(self):
        """If the button "Register" is pressed
The Register Window will run"""
        self.newWindow = Toplevel(self.master)
        self.app = REGWindow(self.newWindow)

    def Forgotwindow(self):
        """If the button "Forgotpass" is pressed
The Forgotpass Window will run"""
        self.newWindow = Toplevel(self.master)
        self.app = FORGWindow(self.newWindow)
#########################################################################################################################################
##                       Loading the Maze_Game in this roots main loop                                                                 ##
#########################################################################################################################################
    def clear(self):
        """This goes through all of
the grids slaves for the Login window
and deletes them so it can run
the Maze_Game"""
        lists = self.master.grid_slaves()
        for l in lists:
            l.destroy()
#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                        REGISTERING AN ACCOUNT WINDOW FOR A NEW USER                                                 ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
######################################################################################################################################### 
class REGWindow:
#########################################################################################################################################
##                             Initializing the account Register Window                                                                                                        ##
#########################################################################################################################################
    def __init__(self, master):
        #This sets the self.master
        self.master = master
        #This sets the title, background and icon
        master.configure(background = "#959595")
        self.master.title("Register")
        self.master.iconbitmap("login.ico")
        #This sets the Labels, Entries and Buttons
        self.lblname = Label(master, text="Name", fg="black", bg="#959595", font=("Helvetica", 12, "underline"))
        self.lblname.grid(row=0)
        self.lblpass = Label(master, text="Pass", fg="black", bg="#959595", font=("Helvetica", 12, "underline"))
        self.lblpass.grid(row=1)
        self.lblq = Label(master, text="Enter your favourite colour", bg="#959595", font=("Helvetica", 12, "underline"))
        self.lblq.grid(row=3, columnspan=3)
        self.btnreg = Button(master, text="Register", command=self.Register, font=('Helvetica', 10, "bold"), relief='flat', bg="#D94A68")
        self.btnreg.grid(row=6, column=3)
        self.entname = Entry(master)
        self.entname.grid(row=0, column=1)
        self.entpass = Entry(master, show="*")
        self.entpass.grid(row=1, column=1)
        self.entq = Entry(master)
        self.entq.grid(row=4, column=1)
#########################################################################################################################################
##                          Register an account Methos                                                                                 ##
#########################################################################################################################################
    def Register(self):
        """This will get the entry
requests for the new user and then check
if it is already been used. If there isnt
a user who is using any of the entrys(not including the passsword)
then the username and pass word will be added to the
login_data.txt, which is stored as a dictionary. The SQ will be
stored in its own file with the username.txt as its file name, so it
can be easily accessed and searched for incase the password
has been forgotten."""
        global users
        username = self.entname.get()
        password = self.entpass.get()
        Security_Q = self.entq.get()
        if username in users:
            messagebox.showerror("ERROR", "Login name already exists")
        elif username == "":
            messagebox.showerror("ERROR", "Please enter a login name")
        elif password == "":
            messagebox.showerror("ERROR", "Please enter a Password")
        else:
            users[username] = password
            with open("login_data.txt", "w") as login_file:
                json.dump(users, login_file)
            with open(username + ".txt", "w") as forgot_pass:
                json.dump(Security_Q, forgot_pass)
            self.master.destroy()
#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                     FORGOT PASSWORD WINDOW INCASE YOU FORGOT YOUR PASSWORD                                          ##
##                                                    FOR YOUR ACCOUNT                                                                 ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
######################################################################################################################################### 
class FORGWindow:
#########################################################################################################################################
##                               Initializing the ForgotPassword Window                                                                ##
#########################################################################################################################################    
    def __init__(self, master):
        #This sets the self.master
        self.master = master
        #This sets the windows title, background coour, and icon
        master.configure(background = "#959595")
        self.master.title("Forgot Password")
        self.master.iconbitmap("login.ico")
        #This sets the Labels, buttons and entries
        self.lbln = Label(master, text="Name",bg="#959595", font=('Helvetica', 12, "underline"))
        self.lbln.grid(row = 0, column = 0)
        self.lblq = Label(master, text="Enter your favourite colour", bg="#959595", font=('Helvetica', 12, "underline"))
        self.lblq.grid(row = 1, columnspan = 2)
        self.entname = Entry(master)
        self.entname.grid(row=0, column = 1)
        self.entq = Entry(master, show="*")
        self.entq.grid(row=2, column = 1)
        self.btn = Button(master, text="OK", command=self.forgot, font=('Helvetica', 10, "bold"), relief='flat', bg="#4B62E0")
        self.btn.grid(row=3, columnspan=2)
#########################################################################################################################################
##                         Fortgot Password Method                                                                                     ##
#########################################################################################################################################        
    def forgot(self):
        """This will take the username
and if there is a user with that name, it will
open their security question file and then check
if the security question matches the one in the file.
If it doesnt then an error message box will appear.
If the user is not registered then an Error messagebox will
also appear."""
        global users
        username = self.entname.get()
        answer = self.entq.get()
        try:
            with open(username + ".txt", "r") as forgot_pass:
                forgot = json.load(forgot_pass)
            if answer == forgot:
                messagebox.showinfo("Password", users[username])
                self.master.destroy()
            else:
                messagebox.showerror("ERROR", "Wrong Colour")
        except:
            messagebox.showerror("ERROR", "User was not Found!")
#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                         CREATE A NEW GAME SAVE OR LOAD A PREVIOUS SAVE                                              ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
######################################################################################################################################### 
class LoadorSave:
#########################################################################################################################################
##                              Initializing the Load or Save Window                                                                   ##
#########################################################################################################################################
    def __init__(self, master):
        #This sets the self.master
        self.master = master
        #This sets the window title, background, icon and minimum size
        self.master.configure(background = "#959595")
        self.master.title("Load")
        self.master.iconbitmap("thanja.ico")
        self.master.minsize(150, 150)
        #This sets all of the labels and buttons
        self.lbl = Label(master, text="Would you like to start", bg="#959595", font=('Helvetica', 12))
        self.lbl1 = Label(master, text="A New Game or", bg="#959595", font=('Helvetica', 12))
        self.lbl2 = Label(master, text="Load an old Game", bg="#959595", font=('Helvetica', 12))
        self.lbl.grid(row=0, columnspan=2)
        self.lbl1.grid(row=1, columnspan=2)
        self.lbl2.grid(row=2, columnspan=2)
        self.btnNew = Button(master, text="New Game", command=self.New_Game, font=('Helvetica', 10, "bold"), relief='flat', bg="#F0A757")
        self.btnNew.grid(row=4, column=0)
        self.btnLoad = Button(master, text="Load Game", command=self.Load_Game, font=('Helvetica', 10, "bold"), relief='flat', bg="#F0A757")
        self.btnLoad.grid(row=4, column=1)
        
#########################################################################################################################################
##                              Creating a new Save file for the User                                                                  ##
#########################################################################################################################################
    def New_Game(self):
        """There is an array
called savearr, and this array stores
the position, inventory and quests that each
user has, and with this the game will know where the
user is in the game. So when a new_Game is set up
this code will create a file with the users name+_save1.txt and
then dump the savearr array with all of the starting position
values. Then it will change the MyGui to = the Maze_Game and then
destroy itself"""
        self.Globals()
        global savearr
        savearr = [[0,0], [], []]
        with open(crntLogin + "_save1.txt", "w") as newgame:
                json.dump(savearr, newgame)
        MyGui = Maze_Game(root)
        self.master.destroy()
#########################################################################################################################################
##                               Loading the save file for the User                                                                    ##
#########################################################################################################################################        
    def Load_Game(self):
        """There is an array
called savearr, and this array stores
the position, inventory and quests that each
user has, and with this the game will know where the
user is in the game. When Load game is pressed
this script will grab the users name and search
for their save file with the saved savearr array and then
the game will change savearr to = the information inside
the txtfile. Then it will set the Global Loggedin=True, and then
it will set MyGui to the Maze_Game and then destroy itself."""
        self.Globals()
        with open(crntLogin + "_save1.txt", "r") as loadgame:
            global savearr
            savearr = json.load(loadgame)
        Loggedin = True
        MyGui = Maze_Game(root)
        self.master.destroy()

    def Globals(self):
        """This command gives everything
its globals"""
        global savearr
        global Loggedin
        global MyGui
#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                      THE MAZE GAME                                                                                  ##
##                                      DESIGNED AND CODED BY: DECLAN WATTS                                                            ##
##                                      This is the main game/script that runs throught out this Game                                  ##
##                                                                                                                                     ##
##                                                                                                                                     ##
#########################################################################################################################################     
class Maze_Game:
#########################################################################################################################################
##                              Initializing the Maze_Game                                                                             ##
#########################################################################################################################################    
    def __init__(self, master):
        #This sets all of the Globals and the self.master
        self.Globals()
        self.master = master
        #This loads the users save file
        self.Inventory = savearr [1]
        self.Quests = savearr [2]
        self.directions = []
        self.ypos = savearr [0][0]
        self.xpos = savearr [0][1]
        #Setting the Background
        self.background_image = PhotoImage(file="Mountain.gif")
        self.background_Label = Label(master, image=self.background_image)
        self.background_Label.place(x=0, y=0, relwidth=1, relheight=1)
        #This sets the windows title and icon
        self.master.title(crntLogin)
        self.master.iconbitmap("thanja.ico")
        #This sets all of the Text Labels
        self.lbl = Label(master, text="Testing, phase", bg="#4B62E0", font=('Helvetica', 12))
        self.lbl.grid(row=1, columnspan=5)
        self.lblarea = Label(master, text="", bg="#4B62E0")
        self.lblarea.grid(row=2, columnspan=5)
        #This sets all of the Buttons
        self.btnNorth = Button(master, text="North", command=self.inactive, font=('Helvetica', 10, "bold"), relief ="flat", bg="#D94A68")
        self.btnNorth.grid(row=3, column=2)
        self.btnSouth = Button(master, text="South", command=self.inactive, font=('Helvetica', 10, "bold"), relief ="flat", bg="#D94A68")
        self.btnSouth.grid(row=5, column=2)
        self.btnEast = Button(master, text="East", command=self.inactive, font=('Helvetica', 10, "bold"), relief ="flat", bg="#D94A68")
        self.btnEast.grid(row=4, column=3)
        self.btnWest = Button(master, text="West", command=self.inactive, font=('Helvetica', 10, "bold"), relief ="flat", bg="#D94A68")
        self.btnWest.grid(row=4, column=1)
        self.btnSave = Button(master, text="Save", command=self.Save_Game, font=('Helvetica', 10, "bold"), relief ="flat", bg="#D94A68")
        self.btnSave.grid(row=6, column=3)
        self.btnLogout = Button(master, text="Log Out", command=self.Logout, font=('Helvetica', 10, "bold"), relief ="flat", bg="#D94A68")
        self.btnLogout.grid(row=6, column=1)
        #This Sets the 2 images that you see
        self.images= PhotoImage(file="banner.gif")
        self.lblpic = Label(master, image=self.images)
        self.lblpic.grid(row=0, columnspan=5)
        #This sets the Minsize for the program
        self.master.minsize(298, 298)
        #This puts spacing in the rows
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(4, weight=1)
        #This runs the runcommands function
        self.runcommands()
#########################################################################################################################################
##                                     Running Commands and Globals                                                                    ##
#########################################################################################################################################
    def runcommands(self):
        """This runs all of the
Globals, Position function, BtnRest fnc,
and checkdirfnc, so it doesnt all have to
be repeated the the program can be
kept DRY. Then at a certain point in the game
This code will also start the first quest."""
        self.Globals()
        self.Position()
        self.Btn_Reset()
        self.checkdir()
        self.background()
        ################
        #Starting Quest#
        ################
        if self.room == "13" and self.Quests == []:
            self.Quests.append("GetNZTicket")
        if "GetNZTicket" in self.Quests:
            self.Questcom()

    def Globals(self):
        """This command gives everything
its globals"""
        global arr
        global savearr
        global crntLogin
#########################################################################################################################################
##                                    Buttons and Label configs                                                                        ##
#########################################################################################################################################
    def inactive(self):
        """When the user
cant move in a certain direction and the
button and the user pressed the button,
a showerror messagebox will show."""
        messagebox.showerror("ERROR", "This is not an available movement in this location")
         
    def North(self):
        """This will change the
y position value to -1 and that
will end up making the user move North
in the array/map. Then it will will
run the command self.rumcommands() to
set all of the values and check for next
available directions and a few more things."""
        self.ypos -= 1
        self.runcommands()        
       
    def South(self):
        """This will change the
y position value to +1 and that
will end up making the user move South
in the array/map. Then it will will
run the command self.rumcommands() to
set all of the values and check for next
available directions and a few more things."""
        self.ypos += 1
        self.runcommands()

    def East(self):
        """This will change the
x position value to +1 and that
will end up making the user move East
in the array/map. Then it will will
run the command self.rumcommands() to
set all of the values and check for next
available directions and a few more things."""
        self.xpos += 1
        self.runcommands()

    def West(self):
        """This will change the
x position value to -1 and that
will end up making the user move West
in the array/map. Then it will will
run the command self.rumcommands() to
set all of the values and check for next
available directions and a few more things."""
        self.xpos -= 1
        self.runcommands()
     
    def Btn_Reset(self):
        """This sets all of the buttons
to have gray text and makes the command that
they do self.inactive"""
        self.btnNorth.config(command=self.inactive, fg="#420DAB", bg="#190A54")
        self.btnSouth.config(command=self.inactive, fg="#420DAB", bg="#190A54")
        self.btnEast.config(command=self.inactive, fg="#420DAB", bg="#190A54")
        self.btnWest.config(command=self.inactive, fg="#420DAB", bg="#190A54")
      
    def checkdir(self):
        """After the Btn_Reset command is run
the maze game will run this code and this code
will change the 2 labels you see, the first label
uses a dictionary with the available directions
for each run through this code because at the end
the dictionary is wiped clean. And then also displays
the type of location the player is in by getting the
text that has been stored in the array. This script will
also runa for_loop and will check in the array for the different
letters that are stored to tell the program the next
available directions.
N = The North Button is set to self.North and
"North" is added to the directions dictionary
S = The South Button is set to self.South and
"South" is added to the directions dictionary
E = The East Button is set to self.East and
"East" is added to the directions dictionary
W = The West Button is set to self.West and
"West" is added to the directions dictionary"""
        self.lblarea.config(text="You are " + self.area)       
        for i in self.opend:
            if i =="N":
                self.btnNorth.config(command=self.North, fg="black", bg="#D94A68")
                self.directions.append("North")
            elif i =="S":
                self.btnSouth.config(command=self.South, fg="black", bg="#D94A68")
                self.directions.append("South")
            elif i =="E":
                self.btnEast.config(command=self.East, fg="black", bg="#D94A68")
                self.directions.append("East")
            elif i =="W":
                self.btnWest.config(command=self.West, fg="black", bg="#D94A68")
                self.directions.append("West")
        txtdir=", ".join(self.directions)
        self.lbl.config(text="You can go " + txtdir)
        self.directions[:] = []

#########################################################################################################################################
##                                   Positioning                                                                                       ##
#########################################################################################################################################            
    def Position(self):
        """This updates all of the
positions after the button is pressed with
the new yposition and the xposition values"""
        self.opend = arr[self.ypos][self.xpos][0]
        self.area = arr[self.ypos][self.xpos][1]
        self.room = arr[self.ypos][self.xpos][2]
        self.BG = arr[self.ypos][self.xpos][3]

#########################################################################################################################################
##                                    Background                                                                                       ##
#########################################################################################################################################
    def background(self):
        """This updates the background"""
        #Sets the Background image
        self.background_image = PhotoImage(file=self.BG + ".gif")
        self.background_Label.config(image=self.background_image)
        


#########################################################################################################################################
##                                    Quests                                                                                           ##
#########################################################################################################################################
    def Questcom(self):
        """This will check what quest
should be next run by checking its requirements
so the code can be more efficient and isnt
always running through every quests if statements."""
        self.Globals()
        if "GetNZTicket" in self.Quests:
            self.GetNZTicket()
        if "GetJob" in self.Quests:
            self.GetJob()
        if "Job" in self.Quests:
            self.Job()

    def GetNZTicket(self):
        """This is the function for
the GetNZTicket Quest"""
        self.Globals() 

        ################
        #Starting Quest#
        ################
        if "10 Gold" not in self.Inventory and self.room == "10":
            self.Quests.append("GetJob")
            messagebox.showinfo("Get Job", """You do not have the money
To afford a ticket from me
Get a Job from a farmer for money""")
        #################    
        #FINISHING QUEST#
        ################# 
        if '10 Gold' in self.Inventory and self.room =="10":
            self.Inventory.append('NzTicket')
            self.Inventory.remove('10 Gold')
            messagebox.showinfo("Ticket", """You have bought
a Ticket to Travel to NewZealand from
the Ticket booth in the city""")
        #################    
        #FINISHING QUEST#
        #################    
        if self.room == "13":
            if 'NzTicket' in self.Inventory:
                messagebox.showinfo("WINNER", "YOU HAVE ESCAPED AND WON")
            else:
                messagebox.showinfo("Ticket", """You have need a ticket
Go to the city to buy one""")

    def GetJob(self):
        """This is the function for
the GetJob Quest"""
        self.Globals()
        ################
        #Starting Quest#
        ################
        if "Job" not in self.Quests and self.room == "8":
            self.Quests.append("Job")
            self.Quests.remove("GetJob")
            messagebox.showinfo("Job", """Hello there
Im in need of assistance
I have a cow that needs to be killed
But I have some jobs to do around town
will you please kill the cow and bring
me the carcase? I will pay you.""")        

    def Job(self):
        """This is the function for
the Job Quest"""
        self.Globals()
        ###############
        #Running Quest#
        ###############
        if "Steak" not in self.Inventory and self.room =="7":
            messagebox.showinfo("Job", """You have seen the cow in the
farm, BATTLE BEGIN!""")
            self.newWindow = Toplevel(self.master)
            self.app = Game(self.newWindow)
        #################    
        #FINISHING QUEST#
        ################# 
        if "Steak" in savearr[1] and self.room =="8":
            self.Quests.remove("Job")
            savearr[1].remove("Steak")
            self.Inventory.append("10 Gold")
            messagebox.showinfo("Job", """Thank you, here is 10 gold""")
#########################################################################################################################################
##                                      Saving/Logging out                                                                             ##
#########################################################################################################################################
    def Save_Game(self):
        """This will grab the savearr
array values and then dump all of it into the
users save file and then display a messagebox
saying that it has been saved"""
        self.Globals()
        savearr=[[self.ypos,self.xpos],self.Inventory,self.Quests]
        with open(crntLogin + "_save1.txt", "w") as newgame:
                json.dump(savearr, newgame)
        messagebox.showinfo("Saved", "Saved!")

    def Logout(self):
        """This will delete all of the
grids slaves and then set MYGui = to Login"""
        lists = self.master.grid_slaves()
        self.Save_Game()
        for l in lists:
            l.destroy()
        MyGui = Login(root)
               
#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                       Battle Clicking Game for the Quest                                                            ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
######################################################################################################################################### 
class Game:
#########################################################################################################################################
##                           Initializing the Clicking battle game Window                                                              ##
#########################################################################################################################################
    def __init__(self, master):
        #This sets the Add Num to 0 and self.master
        self.addnum = 0
        self.master = master
        #This sets the title, background colour and icon
        self.master.title("FIGHT")
        self.master.iconbitmap("fight.ico")
        master.configure(background = "#58b8d8")
        #This sets the Labels, and buttons
        self.score = Label(master, text=int(0), fg="#f4a72c", padx=90)
        self.score.pack(padx=10, pady=10)
        self.button1=Button(master, text="Press me", fg="#f4a72c", command = self.OK, padx=90, pady=30)
        self.button1.pack(padx=10, pady=10)
        self.button2 = Button(master, text="Quit", fg="#f4a72c", command = self.QUIT, padx=90, pady=30)
        self.button2.pack(padx=10, pady=10)
#########################################################################################################################################
##                     The Quit_Game Button                                                                                            ##
#########################################################################################################################################
    def QUIT(self):
        """This will close the clicking program"""
        exit()
#########################################################################################################################################
##                     The Click Me Button                                                                                             ##
#########################################################################################################################################
    def OK(self):
        """When the Press Me button is pressed
then this code will be run, and when the user
reaches a certain number then the cow will be
killed and the user will get the steak to sell to
the farmer to earn the 10gold to buy a ticket to
NewZealand"""
        global savearr
        self.addnum += 1
        self.score.config(text = self.addnum)
        if self.addnum == 105:
           messagebox.showinfo("Job", """Cow has been killed,
return to the farmer""")
           savearr[1].append("Steak")
           self.master.destroy()
#########################################################################################################################################
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                   SETTING ALL OF THE GLOBALS FOR THE CODE AND THEN RUNNING THE TKINTER AND MAINLOOP()                               ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
##                                                                                                                                     ##
#########################################################################################################################################
#########################################################################################################################################
##                   Setting the Login Globals                                                                                         ##
#########################################################################################################################################
Loggedin = False
crntLogin = ""
#########################################################################################################################################
##                  Setting the Arrays for the map and for the save game                                                               ##
#########################################################################################################################################    
arr = [
    [["SE","on a tall Mountain","1","Mountain"],["SEW","beside some Glaciers","2","Glaciers"],["EW","by a cold River","3","Cold_River"],["WS","beside a Lake","4","Lake"]],
    [["NS","beside some Glaciers","5","Glaciers"],["NS","by a cold River","6","Cold_River"],["SE","on some Farm Land","7","Farm_Land"],["NSW","in a Small Town","8","Small_Town"]],
    [["NE","by a Cold River","9","Cold_River"],["NW","in a City","10","City"],["NS","in a Desert","11","Desert"],["NS","heading towards the Departure Dock","12","Dep_Dock"]],
    [["E","Departure dock to NewZealand","13","Nz_Ship"],["EW","by a Beatiful River","14","Beautiful_River"],["NW","surrounded by Beatiful Landscapes","15","Landscapes"],["N","at a ship leaving to Australia, turn around","16","Bad_Ship"]]
    ]

#########################################################################################################################################
##                  Starting and running the Gui                                                                                       ##
#########################################################################################################################################
root = Tk()
MyGui = Login(root)
root.mainloop
