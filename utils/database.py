from .database_connection import DatabaseConnection

"""
All Connections used within the program
"""


def create_user_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(userID INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT,"
                       "username TEXT, password TEXT, trn INTEGER,"
                       "email TEXT, number INTEGER, address TEXT)")


def create_client_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS clients(clientID INTEGER PRIMARY KEY, companyname TEXT, contactperson TEXT, address TEXT, trn INTEGER, email TEXT, number INTEGER)")


def create_records_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS records(recordID INTEGER PRIMARY KEY, amount INTEGER, paymenttype TEXT, paydate INTEGER, paidBy TEXT, clientID INTEGER REFERENCES clients(clientID))")


def find_user(username, password):
    try:
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT userID, firstname, username, password FROM users WHERE username=? AND password = ?", (username, password))
            # user = [cursor.fetchone() #will return tuple with (firstname,lastname,username,password)
            user = cursor.fetchone()
            print(user)
        return user

    except TypeError:
        return None


def add_user(firstname, lastname, username, password, trn, email, number, address):
    create_user_table()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO users VALUES(NULL,?,?,?,?,?,?,?,?)',
                       (firstname, lastname, username, password, trn, email, number, address))


def add_client(companyname, contactperson, address, trn, email, number):
    create_client_table()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO clients VALUES(NULL,?,?,?,?,?,?)',
                       (companyname, contactperson, address, trn, email, number))


def delete_client(clientID):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM clients WHERE clientID = {clientID}')


def find_all_clients():
    try:
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM clients")
            all_clients = cursor.fetchall()
            # name, username, password = user
            print(all_clients)
        return all_clients

    except TypeError:
        return None


def find_all_client_records(clientID):
    try:
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT * FROM records where clientID = {clientID}")
            all_client_records = cursor.fetchall()
            print(all_client_records)
        return all_client_records

    except TypeError:
        return None


def sum_all_receivables(clientID):
    try:
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT SUM(amount) FROM records WHERE clientID = {clientID} AND paymenttype = 'receivable'")
            sum_of_receivables = cursor.fetchone()
            # name, username, password = user
            print(sum_of_receivables)
        return sum_of_receivables

    except TypeError:
        return None


def sum_all_payables(clientID):
    try:
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT SUM(amount) FROM records WHERE clientID = {clientID} AND paymenttype = 'payable'")
            sum_of_payables = cursor.fetchone()
            # name, username, password = user
            print('Rceivables', sum_of_payables)
        return sum_of_payables

    except TypeError:
        return None


def add_record(amount, paymenttype, paydate, paidBy, clientID):
    create_records_table()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO records VALUES(NULL,?,?,?,?,?)',
                       (amount, paymenttype, paydate, paidBy, clientID))


def update_record(amount, paymenttype, paydate, paidBy, recordID, clientID):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        print(amount, paymenttype, paydate, paidBy, recordID, clientID)
        cursor.execute(f'UPDATE records SET amount=?,paymenttype=?,paydate=?,paidBy=? WHERE recordID={recordID}', (
            amount, paymenttype, paydate, paidBy))


def delete_record(recordID):
    create_records_table()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM records WHERE recordID={recordID}')
