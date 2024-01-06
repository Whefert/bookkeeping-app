"""
Author: Jefferson Daley
Date: December 15, 2020
Purpose: Bookeping application that allows users to register, login, add new clients as well as reecvable and payable records for those clients.
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label, PhotoImage
from utils.database import *
from users import *
from datetime import date
from dashboard import *


def aboutapp():
    # Function which provides an overview of the purpose and functionality of the profram
    messagebox.showinfo("About The Bookkepping App",
                        "Purpose: Bookeping application that allows users to register, login, add new clients as well as receivable and payable records for those clients.")


def register_new_user():
    # Function to get data from user registration entry fields then add them to the database
    print(new_user_firstname.get())
    firstname = new_user_firstname.get()
    lastname = new_user_lastname.get()
    username = new_username.get()
    password = new_user_password.get()
    trn = new_user_TRN.get()
    email = new_user_email.get()
    number = new_user_number.get()
    address = new_user_address .get()

    User().register_user(firstname, lastname, username,
                         password, trn, email, number, address)
    register_screen.destroy()


def register_user_window():
    # Function which creates the user registration window to aad new users data

    global new_user_firstname
    # String variable to store the new user's firstname
    new_user_firstname = StringVar()

    global new_user_lastname
    # String variable to store the new user's lasstname
    new_user_lastname = StringVar()

    global new_username
    # String variable to store the new user's username
    new_username = StringVar()

    global new_user_password
    # String variable to store the new user's password
    new_user_password = StringVar()

    global new_user_email
    # String variable to store the new user's email
    new_user_email = StringVar()

    global new_user_number
    # Integer variable to store the new user's phone number
    new_user_number = IntVar()

    global new_user_address
    # String variable to store the new user's address
    new_user_address = StringVar()

    global new_user_TRN
    # Integer variable to store the new user's TRN number
    new_user_TRN = IntVar()

    # Createion of user registration window
    global register_screen
    register_screen = Toplevel(login_win)
    register_screen.title("Register")
    register_screen.geometry("500x250")
    instructions = Label(
        register_screen, text="Please enter your details below to register")
    instructions.pack(pady=(30, 10))

    # Create left and right frame groups to place entry items and labels
    leftgroup = Frame(register_screen)
    leftgroup.pack(side='left', fill="both",
                   expand=True, padx=(30, 10), pady=10)
    rightgroup = Frame(register_screen)
    rightgroup.pack(side='left', fill="both",
                    expand=True, padx=(0, 30), pady=10)

    # User first name label and entry
    user_firstnamelbl = Label(
        leftgroup, text="First Name:", bd=1, justify="left")
    user_firstnamelbl.grid(row=1, column=0, padx=(0, 5))
    user_firstname = Entry(leftgroup, fg='blue',
                           textvariable=new_user_firstname, width=20)
    user_firstname.grid(in_=leftgroup, row=1, column=1, pady=5)
    user_firstname.focus()

    # User email address label and entry
    user_emaillbl = Label(leftgroup, text="Email:", justify="left")
    user_emaillbl.grid(row=2, column=0, padx=(0, 5))
    user_useremail = Entry(leftgroup, fg='blue',
                           textvariable=new_user_email, width=20)
    user_useremail.grid(in_=leftgroup, row=2, column=1, pady=5)

    # User address label and entry
    user_addresslbl = Label(leftgroup, text="Address:", justify="left")
    user_addresslbl.grid(row=3, column=0, padx=(0, 5))
    user_address = Entry(leftgroup, fg='blue',
                         textvariable=new_user_address, width=20)
    user_address.grid(in_=leftgroup, row=3, column=1, pady=5)

    # Username label and entry
    usernamelbl = Label(leftgroup, text="Username:", justify="left")
    usernamelbl.grid(row=4, column=0, padx=(0, 5), sticky="w")
    username = Entry(leftgroup, fg='blue', textvariable=new_username, width=20)
    username.grid(in_=leftgroup, row=4, column=1, pady=5)

    # User last name label and entry
    user_lastnamelbl = Label(
        rightgroup, text="Last Name:", bd=1, justify="left")
    user_lastnamelbl.grid(row=1, column=0, padx=(0, 5))
    user_lastname = Entry(rightgroup, fg='blue',
                          textvariable=new_user_lastname, width=20)
    user_lastname.grid(in_=rightgroup, row=1, column=1, pady=5)

    # User phone number address label and entry
    user_numberlbl = Label(rightgroup, text="Phone Number:", justify="left")
    user_numberlbl.grid(row=2, column=0, padx=(0, 5))
    user_number = Entry(rightgroup, fg='blue',
                        textvariable=new_user_number, width=20)
    user_number.grid(in_=rightgroup, row=2, column=1, pady=5)

    # User TRN# label and entry
    user_TRNlbl = Label(rightgroup, text="TRN#:", justify="left")
    user_TRNlbl.grid(row=3, column=0, padx=(0, 5))
    user_TRN = Entry(rightgroup, fg='blue',
                     textvariable=new_user_TRN, width=20)
    user_TRN.grid(in_=rightgroup, row=3, column=1, pady=5)

    # User password label and entry
    user_passwordlbl = Label(rightgroup, text="Password:", justify="left")
    user_passwordlbl.grid(row=4, column=0, padx=(0, 5))
    user_password = Entry(rightgroup, show="*", fg='blue',
                          textvariable=new_user_password, width=20)
    user_password.grid(in_=rightgroup, row=4, column=1, pady=5)

    # Button to create a user account
    createAccountBtn = Button(
        leftgroup, text="Create Account", justify="left", command=register_new_user, fg='white', bg='#01D132')
    createAccountBtn.grid(in_=leftgroup, row=5, column=0,
                          pady=10, columnspan=6, ipady=3, ipadx=10, sticky="w")
    # Consider for adding image


def login_user():
    # Function to validate user login credentials that have been input on login screen

    # Storing username and password values(strings) input by user in Entry fields
    username_value = username.get()
    userpswd_value = userpswd.get()

    # If statement to test if user login creditianls have been entered and if they are valid
    if username_value and userpswd_value:
        global current_user
        # Use of method from User class to validate login credentials and return list with tuple of user details if user is found. Query will return None if no matching records is found
        current_user = User().login(username_value, userpswd_value)
        # Prompt for user to try again if no record is found to match login credentials entered
        if current_user == None:
            messagebox.showwarning("Incorrect username/password",
                                   "The username/password you entered is incorrect, "
                                   "please try again")

        # Redirect users to dashboard screen if login is succesful. Destroy the login window as it is no longer necessary/relevant
        else:
            login_win.destroy()
            load_dashboard(current_user)
            print("success")

    else:
        # Reminder to client that neither the username nor password fields can be blank when they are submitting login credentials
        messagebox.showwarning(
            "Incomplete Entry", "Please enter your username AND password")


def user_login_window():
    # Creation of login window with username and passowrd entry fields to facilitate user login
    global login_win
    login_win = Tk()

    global username
    global userpswd

    # Creation of textvariables to store data from Entry fields
    username = StringVar()
    userpswd = StringVar()

    # Creation, placement and labelling of main/login window
    login_win.geometry("500x400+500+100")
    login_win.title('Bookkeeping App')
    login_win['background'] = '#FDFDFD'

    # Addition of app logo to add visual interest
    app_logo = PhotoImage(file="Bookkeping App Logo.png")
    app_name = Label(login_win, text='Jeff\'s Bookkeeping App',
                     fg="#25017C", bg="#FDFDFD", font='Roboto 16 bold')

    app_name.pack(pady=(20, 10))
    app_logo_lbl = Label(login_win, bg='#FDFDFD', image=app_logo)
    app_logo_lbl.pack()

    # Creation of frame to neatly store login entry fields
    login_frame = Frame(login_win, bg="#FDFDFD")
    login_frame.pack(pady=20)

    # Creation and placement of username label and entry field
    username_entry_label = Label(
        login_frame, text="Enter Username:", bg="#FDFDFD")
    username_entry_label.grid(row=0, column=0, pady=5, padx=5)
    username_entry = Entry(login_frame, fg='#0F0033', textvariable=username,
                           width=20)
    username_entry.grid(row=0, column=1)
    username_entry.focus()

    # Creation and placement of password label and entry field
    password_entry_label = Label(
        login_frame, text="Enter Password:", bg="#FDFDFD")
    password_entry_label.grid(row=1, column=0, pady=5, padx=5)
    password_entry = Entry(login_frame, show="*", fg='#0F0033', textvariable=userpswd,
                           width=20)
    password_entry.grid(row=1, column=1)

    # Creation of login button which calls function to validate user login credentials entered
    login_btn = Button(login_frame, text='LOGIN', fg='blue',
                       bg='#2699FB', foreground="#FFFFFF", width=30, command=login_user)
    login_btn.grid(row=2, column=0, columnspan=2, pady=5)

    # Creation of instruction text for user to create an account(register) if they don't have one already

    Label(login_win, bg='#FDFDFD',
          text='Don\'t have an account, create one here').pack(pady=(0, 5))

    register_btn = Button(login_win, text='REGISTER',
                          fg='white', bg='#01D132', width=8, command=register_user_window)
    register_btn.pack()

    # Creation of menu bar to facilitate register functions and software overview messagebox loading
    menu = Menu(login_win)
    login_win.configure(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Register', command=register_user_window)

    aboutmenu = Menu(menu)
    menu.add_cascade(label='About', menu=aboutmenu)
    aboutmenu.add_command(label='About App', command=aboutapp)

    login_win.mainloop()


user_login_window()
