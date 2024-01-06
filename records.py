from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Label, PhotoImage
from utils.database import *


class Record:
    # Class created to store most methods related to client accounts
    def __init__(self, record):
        # initialization to store data retrieved from each record in the database
        self.record = record
        print(self.record)
        self.recordID = record[0]
        print
        self.recordamount = record[1]
        self.paymenttype = record[2]
        self.paydate = record[3]
        self.paidBy = record[4]
        self.clientID = record[5]

    def create_record_frame(self, parent):
        # Create and placement of record card frame to neatly store record data in view client records window
        record_card = Frame(parent, borderwidth=1,
                            relief="sunken", pady=10)
        record_card.pack(fill="x")

        # Get and show record payment type
        paymenttype = self.paymenttype
        recordpaymenttypelbl = Label(
            record_card, text=paymenttype, width=10)
        recordpaymenttypelbl.grid(row=0, column=0, padx=5)

        #  Get and show record amount
        recordamount = self.recordamount
        recordamountlbl = Label(record_card, text=recordamount, width=10,)
        recordamountlbl.grid(row=0, column=1, padx=5)

        #  Get and show record paydate
        paymentdate = self.paydate
        recordpaymentdatelbl = Label(
            record_card, text=paymentdate, width=15)
        recordpaymentdatelbl.grid(row=0, column=2, padx=5)

        # Button creationg and placement to facilitate the editing of the record
        edit_client_record = self.edit_client_record_func
        edit_record_button = Button(record_card,  text='Edit', fg='blue',
                                    bg='#9EAE00', foreground="#FFFFFF", width=10, command=edit_client_record
                                    )
        edit_record_button.grid(row=0, column=3, padx=5)

        # Button creationg and placement to facilitate record deletion
        delete_record = self.delete_record_func
        delete_record_btn = Button(record_card, text='Delete', fg='blue',
                                   bg='red', foreground="#FFFFFF", width=10,
                                   command=delete_record)
        delete_record_btn.grid(row=0, column=4, padx=(7, 0), pady=10)

    def delete_record_func(self):
        # function to confirm deletion request and remove the record from the database
        confirmation = messagebox.askyesno(
            "Please confirm", "Are you sure you want to delete this record?")
        if confirmation:
            recordID = self.recordID
            delete_record(recordID)
        else:
            return ""

    def edit_client_record_func(self):
        # creation of window to facilitate the editing of each record
        global edited_record_amount
        # Int variable to store the editied record amount
        edited_record_amount = IntVar()

        global edited_record_paymenttype
        # String variable to store the editied record paymenttype
        edited_record_paymenttype = StringVar()

        global edited_record_paydate
        # String variable to store the editied record paymentdate
        edited_record_paydate = StringVar()

        global edited_record_paidBy
        # String variable to store the editied record paidBy
        edited_record_paidBy = StringVar()

        global edited_record_clientID
        # Integer variable to store the editied record's client ID
        edited_record_clientID = IntVar()

        global edit_client_record
        # creationg and placement of the window to house the edit entry record fields
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
        current_amount = self.recordamount
        print(current_amount)
        edit_record_amountlbl = Label(
            entry_item_container, text="Amount:", bd=1, justify="left")
        edit_record_amountlbl.grid(row=0, column=0, padx=(0, 5))
        edit_record_amount = Entry(entry_item_container, fg='blue',
                                   textvariable=edited_record_amount, width=20)
        edit_record_amount.grid(row=0, column=1, pady=5)
        edit_record_amount.focus()
        edited_record_amount.set(current_amount)

        # Record payment type label and entry
        current_paymenttype = self.paymenttype
        edit_record_paymenttypelbl = Label(
            entry_item_container, text="Payment Type:", bd=1, justify="left")
        edit_record_paymenttypelbl.grid(row=1, column=0, padx=(0, 5))
        edit_record_paymenttype = Entry(entry_item_container, fg='blue',
                                        textvariable=edited_record_paymenttype, width=20)
        edit_record_paymenttype.grid(row=1, column=1, pady=5)
        edited_record_paymenttype.set(current_paymenttype)

        # Record pay date type label and entry
        current_paydate = self.paydate
        edit_record_paydatelbl = Label(
            entry_item_container, text="Pay Date:", bd=1, justify="left")
        edit_record_paydatelbl.grid(row=2, column=0, padx=(0, 5))
        edit_record_paydate = Entry(entry_item_container, fg='blue',
                                    textvariable=edited_record_paydate, width=20)
        edit_record_paydate.grid(row=2, column=1, pady=5)
        edited_record_paydate.set(current_paydate)

        # Record paid by label and entry
        current_paidBy = self.paidBy
        edit_record_paidBylbl = Label(
            entry_item_container, text="Paid By:", bd=1, justify="left")
        edit_record_paidBylbl.grid(row=3, column=0, padx=(0, 5))
        edit_record_paidBy = Entry(entry_item_container, fg='blue',
                                   textvariable=edited_record_paidBy, width=20)
        edit_record_paidBy.grid(row=3, column=1, pady=5)
        edited_record_paidBy.set(current_paidBy)

        update_client_record = self.update_client_record_func
        add_recordBtn = Button(edit_client_record, text='Update Record', fg='blue',
                               bg='#2699FB', foreground="#FFFFFF", width=20, command=update_client_record)
        add_recordBtn.pack(pady=(10, 20))

    def update_client_record_func(self):
        # function to collect record edit entries and commit them to the database with an sql query
        amount = edited_record_amount.get()
        paymenttype = edited_record_paymenttype.get()
        paydate = edited_record_paydate.get()
        paidBy = edited_record_paidBy.get()
        clientID = self.clientID

        confirmation = messagebox.askyesno(
            "Please confirm", "Are you sure you want to update this record?")
        if confirmation:
            recordID = self.recordID
            print(recordID)
            update_record(amount, paymenttype, paydate,
                          paidBy, recordID, clientID)
        else:
            return ""
