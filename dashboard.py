from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label, PhotoImage
from utils.database import *
from datetime import date
from client import *


def create_new_client():
    # Function to collect new client data entered and add it to the database
    companyname = new_companyname.get()
    contactperson = new_clientcontactperson.get()
    address = new_client_address.get()
    trn = new_client_TRN.get()
    email = new_client_email.get()
    number = new_client_number.get()

    # Database insert query to add data from new client entry fields to database
    add_client(companyname, contactperson, address, trn, email, number)
    messagebox.showinfo(
        title="Success", message="Account created successfully")
    add_new_client.destroy()


def add_new_client_window():

    global add_new_client
    add_new_client = Toplevel()

    add_new_client.title("Add New Client")
    add_new_client.geometry("500x250")
    instructions = Label(
        add_new_client, text="Please enter the new client's details below", foreground="black")
    instructions.pack(pady=(30, 10))

    # Creates registration login_window to add new clients
    global new_companyname
    # String variable to store the new company's name
    new_companyname = StringVar()

    global new_clientcontactperson
    # String variable to store the new company contact persons' name
    new_clientcontactperson = StringVar()

    global new_client_address
    # String variable to store the new company's address
    new_client_address = StringVar()

    global new_client_email
    # String variable to store the new company's email
    new_client_email = StringVar()

    global new_client_number
    # Integer variable to store the new company's phone number
    new_client_number = IntVar()

    global new_client_TRN
    # Integer variable to store the new company's business TRN
    new_client_TRN = IntVar()

    # Create left and right frame groups to neatly place entry items and labels in add_new_client window
    leftgroup = Frame(add_new_client)
    leftgroup.pack(side='left', fill="both",
                   expand=True, padx=(30, 10), pady=10)
    rightgroup = Frame(add_new_client)
    rightgroup.pack(side='left', fill="both",
                    expand=True, padx=(0, 30), pady=10)

    # client first name label and entry
    client_namelbl = Label(leftgroup, text="Company Name:",
                           bd=1, justify="left")
    client_namelbl.grid(row=1, column=0, padx=(0, 5))
    client_name = Entry(leftgroup, fg='blue',
                        textvariable=new_companyname, width=20)
    client_name.grid(in_=leftgroup, row=1, column=1, pady=5)
    client_name.focus()

    # client email address label and entry
    client_emaillbl = Label(leftgroup, text="Email:", justify="left")
    client_emaillbl.grid(row=2, column=0, padx=(0, 5))
    client_clientemail = Entry(
        leftgroup, fg='blue', textvariable=new_client_email, width=20)
    client_clientemail.grid(in_=leftgroup, row=2, column=1, pady=5)

    # client address label and entry
    client_addresslbl = Label(leftgroup, text="Address:", justify="left")
    client_addresslbl.grid(row=3, column=0, padx=(0, 5))
    client_address = Entry(leftgroup, fg='blue',
                           textvariable=new_client_address, width=20)
    client_address.grid(in_=leftgroup, row=3, column=1, pady=5)

    # client contact person label and entry
    client_clientcontactpersonlbl = Label(
        rightgroup, text="Contact Person:", justify="left")
    client_clientcontactpersonlbl.grid(row=1, column=0, padx=(0, 5))
    client_clientcontactperson = Entry(rightgroup, fg='blue',
                                       textvariable=new_clientcontactperson, width=20)
    client_clientcontactperson.grid(
        in_=rightgroup, row=1, column=1, pady=5)

    # client phone number address label and entry
    client_numberlbl = Label(
        rightgroup, text="Phone Number:", justify="left")
    client_numberlbl.grid(row=2, column=0, padx=(0, 5))
    client_number = Entry(rightgroup, fg='blue',
                          textvariable=new_client_number, width=20)
    client_number.grid(in_=rightgroup, row=2, column=1, pady=5)

    # client TRN# label and entry
    client_TRNlbl = Label(rightgroup, text="TRN#:", justify="left")
    client_TRNlbl.grid(row=3, column=0, padx=(0, 5))
    client_TRN = Entry(rightgroup, fg='blue',
                       textvariable=new_client_TRN, width=20)
    client_TRN.grid(in_=rightgroup, row=3, column=1, pady=5)

    # Button with function to create a new client account
    createAccountBtn = Button(
        leftgroup, text="Create Account", justify="left", bg='#01D132', command=create_new_client
    )
    createAccountBtn.grid(row=4, column=0,
                          pady=5, columnspan=6, ipady=3, ipadx=10, sticky="w")


def load_dashboard(current_user):
    # Funtion to load user dashboard that allows user to choose which client to work on
    global session
    global user

    # Creationg of global user variable to allow for personalized greetings across the app
    user = current_user

    # Creation and placement of dashboard(session) window to facilitate client rendering on screen and choice
    session = Tk()
    session.geometry("500x400+500+100")
    session.title("Dashboard")
    session['background'] = '#FDFDFD'

    # Variable creation to store and show the date on the dashboard
    today = date.today().strftime("%d/%m/%Y")
    user_first_name = user[1]

    # Creation and placement of personalized greeting for user on dashboard screen
    greeting = Label(session, text=f"Hi {user_first_name}\n {today}  ",
                     justify="right", anchor="e", bg='#FDFDFD')
    greeting.pack(fill="x", padx=20)

    # Instructions label creation and placement to guide users about next possible actions within the app
    instructions = Label(session, text='Please select a client to work on',
                         fg="black", bg="#FDFDFD")
    instructions.pack(pady=(20, 10))
    global clientcontainer
    clientcontainer = Frame(session, bg="#FDFDFD")
    clientcontainer.pack(pady=10)

    # Storage of list clients return return from databse query to find all clients
    all_clients = find_all_clients()

    # List comprehension over all clients to create a Client object for each client. A client frame is created for each object and placed in the clientcontainer window as they are created.
    [Client(client).create_client_frame(clientcontainer)
     for client in all_clients]

    # Creation and placement of button to facilitate the calling of the function to add a new client
    add_client_btn = Button(
        session, text="Add A New Client", command=add_new_client_window, bg='#01D132', width=15)
    add_client_btn.pack(pady=20)

    session.mainloop()
