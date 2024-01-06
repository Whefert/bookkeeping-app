from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label, PhotoImage
from utils.database import *
from datetime import date
from records import *


class Client():
    # creation of class to store and easily call most client methods

    def __init__(self, client):
        # initialization of client class
        self.client = client
        self.clientID = client[0]
        self.companyname = client[1]
        self.records = []

    def create_client_frame(self, parent):
        # function to create the client frame for each client to be dispalyed on the dashboard
        global client_card

        # Client card creation  and placement to neatly hold store client data on the dashbord
        client_card = Frame(parent, borderwidth=1,
                            relief="sunken", pady=10)
        client_card.pack(fill="x")

        # Create left and right frame groups to neatly place client data and buttons on the dashboard

        leftgroup = Frame(client_card)
        leftgroup.pack(side='left', fill="x",
                       expand=True)
        rightgroup = Frame(client_card)
        rightgroup.pack(side='left', fill="x",
                        expand=True, padx=(0, 20))

        # Creation and placement of company name label in client card which in turn is placed on the dashboard
        comapnyname = self.companyname
        comapnynamelbl = Label(leftgroup, text=f"Client: {comapnyname}",
                               font="Roboto 14")
        comapnynamelbl.grid(padx=(30, 0))

        # Creation and placement of delete client button in client card which in turn is placed on the dashboard
        delete_client = self.delete_client_func
        delete_client_btn = Button(rightgroup, text='Delete Client', fg='blue',
                                   bg='red', foreground="#FFFFFF", width=10,
                                   command=delete_client)
        delete_client_btn.pack(side="right", padx=1)

        # Creation and placement of view client button in client card which in turn is placed on the dashboard. This button allows the user to view all records associated with the client.
        view_client_records = self.view_client_records
        viewRecordsBtn = Button(rightgroup, text='View Records', fg='blue',
                                bg='#2699FB', foreground="#FFFFFF", width=10, command=view_client_records)
        viewRecordsBtn.pack(side="right", padx=1)

    def view_client_records(self):
        # function to create the client window that allows users to view records associated with each client

        global view_client_records

        # creation and placement of client records window to show all client records
        view_client_records = Toplevel()
        view_client_records['background'] = "white"

        # querry database for all records related to the client ID
        view_client_records.title(f"Client: {self.clientID}")

        # Create client window
        view_client_records.geometry("500x400")

        # Identify client account that is currently being worked on
        clientname = self.companyname
        client_name_lbl = Label(
            view_client_records, text=clientname, font="Roboto 16", bg="white", justify="left")
        client_name_lbl.pack(fill="x")

        # Create frame for overview tab that presents high level metrics
        overview = Frame(view_client_records, bg="white")
        overview.pack(pady=10)

        # Function call to sum and return all receivables related to the client
        receivables = sum_all_receivables(self.clientID)[0]
        total_receivables = receivables

        # Function call to sum and return all payables related to the client
        payables = sum_all_payables(self.clientID)[0]
        total_payables = payables

        # Function to et and show account balance metric
        calc_account_balance = self.calc_account_balance_func
        account_balance = calc_account_balance(
            total_receivables, total_payables)

        # Change account balance colour based on positive or negative balance
        account_status_colour = ""
        if account_balance == None:
            account_status_colour = "black"
        elif account_balance < 0:
            account_status_colour = "red"
        else:
            account_status_colour = "green"

        account_balancelbl = Label(
            overview, text=f"Account Balance:\n ${account_balance}", bg=account_status_colour, fg="white")
        account_balancelbl.pack(side="left", padx=(10))

        # Get and show total receivables
        total_receivableslbl = Label(
            overview, text=f"Total Receivables:\n ${total_receivables}", bg="white")
        total_receivableslbl.pack(side="left", padx=(10))

        # Get and show total payables
        total_payableslbl = Label(
            overview, text=f"Total Payables:\n ${total_payables}", bg="white")
        total_payableslbl.pack(side="left", padx=(10))

        # Creare frame for tab headings
        tab_headings = Frame(view_client_records, relief="sunken")
        tab_headings.pack()

        # Create heading/label for record type column
        recordtypelbl = Label(tab_headings, text="Type", borderwidth=1)
        recordtypelbl.pack(side="left", padx=(0, 40))

        # Create heading/label for record amount column
        recordamountlbl = Label(tab_headings, text="Amount")
        recordamountlbl.pack(side="left", padx=(0, 20))

        # Create heading/label for record date column
        recorddatelbl = Label(tab_headings, text="Payment Date")
        recorddatelbl.pack(side="left", padx=(17, 20))

        # Create heading/label for modify record column
        edit_record_lbl = Label(tab_headings, text="Edit")
        edit_record_lbl.pack(side="left", padx=(30, 30))

        # Create heading/label for deleting record column
        recorddeletelbl = Label(tab_headings, text="Delete")
        recorddeletelbl.pack(side="left", padx=(30, 0))

        records_container = Frame(view_client_records, bg="#FDFDFD")
        records_container.pack()

        # Find all client records
        clientID = self.clientID
        all_client_records = find_all_client_records(clientID)

        [Record(record).create_record_frame(records_container)
         for record in all_client_records]

        # Button creation and placement which facilitates function to generate records
        add_client_record = self.add_client_record_func
        btnRegister = Button(view_client_records, text='Add New Record',
                             fg='white', bg='#01D132',
                             command=add_client_record
                             )
        btnRegister.pack(pady=10)

    def add_client_record_func(self):
        # function to create window for user entry fields to add client records to the database

        global record_amount
        # Integer variable to store the record amount to be added
        record_amount = IntVar()

        global record_paymenttype
        # String variable to store the record payment type
        record_paymenttype = StringVar()

        global record_paydate
        # String variable to store the record payment date to be added
        record_paydate = StringVar()

        global record_paidBy
        # String variable to store name of who the record was paid by
        record_paidBy = StringVar()

        global record_clientID
        # Integer variable to store the clientID associated with the record
        record_clientID = IntVar()

        global add_client_record_win
        # Creation and placement of window to facilitate new record data entry
        add_client_record_win = Toplevel()
        add_client_record_win.geometry("300x250")
        add_client_record_win.title("Add New Record")
        instructions = Label(
            add_client_record_win, text="Please enter the record details below")
        instructions.pack(pady=(20, 10))

        # Create container for record entry fields
        entry_item_container = Frame(add_client_record_win)
        entry_item_container.pack()

        # Record amound label and entry
        new_record_amountlbl = Label(
            entry_item_container, text="Amount:", bd=1, justify="left")
        new_record_amountlbl.grid(row=0, column=0, padx=(0, 5))
        new_record_amount = Entry(entry_item_container, fg='blue',
                                  textvariable=record_amount, width=20)
        new_record_amount.grid(row=0, column=1, pady=5)
        new_record_amount.focus()

        # Record payment type label and entry
        new_record_paymenttypelbl = Label(
            entry_item_container, text="Payment Type:", bd=1, justify="left")
        new_record_paymenttypelbl.grid(row=1, column=0, padx=(0, 5))
        new_record_paymenttype = Entry(entry_item_container, fg='blue',
                                       textvariable=record_paymenttype, width=20)
        new_record_paymenttype.grid(row=1, column=1, pady=5)

        # Record pay date type label and entry
        new_record_paydatelbl = Label(
            entry_item_container, text="Pay Date:", bd=1, justify="left")
        new_record_paydatelbl.grid(row=2, column=0, padx=(0, 5))
        new_record_paydate = Entry(entry_item_container, fg='blue',
                                   textvariable=record_paydate, width=20)
        new_record_paydate.grid(row=2, column=1, pady=5)

        # Record paid by label and entry
        new_record_paidBylbl = Label(
            entry_item_container, text="Paid By:", bd=1, justify="left")
        new_record_paidBylbl.grid(row=3, column=0, padx=(0, 5))
        new_record_paidBy = Entry(entry_item_container, fg='blue',
                                  textvariable=record_paidBy, width=20)
        new_record_paidBy.grid(row=3, column=1, pady=5)

        insert_new_record = self.insert_new_record_func
        add_recordBtn = Button(add_client_record_win, text='Add Record', fg='blue',
                               bg='#2699FB', foreground="#FFFFFF", width=10,
                               command=insert_new_record
                               )
        add_recordBtn.pack(pady=(10, 20))

    def insert_new_record_func(self):
        # function to receive data from entry fields on new record window and add them to the records table in the database
        amount = record_amount.get()
        paymenttype = record_paymenttype.get()
        paydate = record_paydate.get()
        paidBy = record_paidBy.get()
        clientID = self.clientID

        # Database querry to add new record
        add_record(amount, paymenttype, paydate, paidBy, clientID)
        messagebox.showinfo(
            title="Success", message="Record added successfully")
        add_client_record_win.destroy()
        print("success")

    def calc_account_balance_func(self, receivables, payables):
        # function to calculate account balance based on existing or non-existing receivables and payables
        if receivables and payables:
            balance = receivables - payables
            return balance
        elif receivables == None:
            return payables
        elif payables == None:
            return receivables
        else:
            return 0

    def edit_client_record_func(self):
        # function to create window to facilitate client record updating
        global edited_record_amount
        edited_record_amount = IntVar()

        global edited_record_paymenttype
        edited_record_paymenttype = StringVar()

        global edited_record_paydate
        edited_record_paydate = StringVar()

        global edited_record_paidBy
        edited_record_paidBy = StringVar()

        global edited_record_clientID
        edited_record_clientID = IntVar()

        global edit_client_record
        edit_client_record = Toplevel()
        edit_client_record.geometry("300x250")
        edit_client_record.title("Edit Client Record")
        instructions = Label(
            edit_client_record, text="Please change the record details below as needed")
        instructions.pack(pady=(20, 10))

        # Create container for record entry fields
        entry_item_container = Frame(edit_client_record)
        entry_item_container.pack()

        # Record amound label and entry
        edit_record_amountlbl = Label(
            entry_item_container, text="Amount:", bd=1, justify="left")
        edit_record_amountlbl.grid(row=0, column=0, padx=(0, 5))
        edit_record_amount = Entry(entry_item_container, fg='blue',
                                   textvariable=edited_record_amount, width=20)
        edit_record_amount.grid(row=0, column=1, pady=5)
        edit_record_amount.focus()

        # Record payment type label and entry
        edit_record_paymenttypelbl = Label(
            entry_item_container, text="Payment Type:", bd=1, justify="left")
        edit_record_paymenttypelbl.grid(row=1, column=0, padx=(0, 5))
        edit_record_paymenttype = Entry(entry_item_container, fg='blue',
                                        textvariable=edited_record_paymenttype, width=20)
        edit_record_paymenttype.grid(row=1, column=1, pady=5)

        # Record pay date type label and entry
        edit_record_paydatelbl = Label(
            entry_item_container, text="Pay Date:", bd=1, justify="left")
        edit_record_paydatelbl.grid(row=2, column=0, padx=(0, 5))
        edit_record_paydate = Entry(entry_item_container, fg='blue',
                                    textvariable=edited_record_paydate, width=20)
        edit_record_paydate.grid(row=2, column=1, pady=5)

        # Record paid by label and entry
        edit_record_paidBylbl = Label(
            entry_item_container, text="Paid By:", bd=1, justify="left")
        edit_record_paidBylbl.grid(row=3, column=0, padx=(0, 5))
        edit_record_paidBy = Entry(entry_item_container, fg='blue',
                                   textvariable=edited_record_paidBy, width=20)
        edit_record_paidBy.grid(row=3, column=1, pady=5)

        update_client_record = self.update_client_record_func
        add_recordBtn = Button(edit_client_record, text='Update Record', fg='blue',
                               bg='#2699FB', foreground="#FFFFFF", width=10, command=update_client_record)
        add_recordBtn.pack(pady=(10, 20))

    def update_client_record_func(self):

        amount = record_amount.get()
        paymenttype = record_paymenttype.get()
        paydate = record_paydate.get()
        paidBy = record_paidBy.get()
        clientID = self.clientID

        add_record(amount, paymenttype, paydate, paidBy, clientID)
        messagebox.showinfo(
            title="Success", message="Record added successfully")
        add_client_record_win.destroy()
        print("success")

    def delete_client_func(self):
        confirmation = messagebox.askyesno(
            "Please confirm", "Are you sure you want to delete this client?")
        if confirmation:
            clientID = self.clientID
            delete_client(clientID)
        else:
            return ""
