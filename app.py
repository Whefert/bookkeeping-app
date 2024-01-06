from utils import database as db
from utils.user_registration import User

def register_user():
    firstname = input("First name: ")
    lastname = input("Last name: ")
    username = input("Username: ")
    password = input("Password: ")

    db.add_user(firstname, lastname,username,password)


def login_user():
    login_username = input("What is your username? ")
    login_password = input("What is your password? ")

    print(db.find_user(login_username, login_password))


def add_client():
    firstname = input("Firstname: ")
    lastname = input("Lastname: ")
    trn = int(input("TRN #: "))
    address = input("Address: ")
    city = input("City: ")

    db.add_client(firstname,lastname,trn,address, city)

def add_payable():
    amount = int(input("Amount: "))
    paymentType = input("Type: ")
    payDate = int(input('Enter a date in YYYY-MM-DD format'))
    paidBy = input("Paid By: ")
    clientID = int(input("Client: "))

    db.add_payable(amount, paymentType, payDate, paidBy, clientID)

# register_user()
# login_user()
# add_client()

add_payable()