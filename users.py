from utils.database import *
from tkinter import messagebox, Label, PhotoImage


class User:
    # class to store most methods relating to users
    def __init__(self):
        self.username = ""
        self.userID = ""
        self.firstname = ""
        self.lastname = ""
        self.username = ""
        self.password = ""

    def register_user(self, firstname, lastname, username, password, trn, email,
                      number, address):
        # function to collect user information and add to the database
        add_user(firstname, lastname, username,
                 password, trn, email, number, address)
        messagebox.showinfo(
            title="Success", message="Account created successfully")

    def login(self, username, password):
        # function to validate user login credentials in database
        user = find_user(username, password)
        if user == True:
            self.firstname = user[1]
            self.userID = user[0]
            self
        print(username)
        return user

    @classmethod
    def sfirstname(cls):
        print(cls.__name__)

    print("success")
